# Repository Migration Plan

This plan defines how the prototype repository
`kerer-ai/ttfhw-verify-batch` is split into independent TTFHW repositories.

The prototype is a source of behavior, fixtures, and historical assets. It is
not the target architecture.

## Goals

- make service, runner, data processing, and dashboard deploy independently
- preserve useful verification behavior and historical report data
- remove runtime coupling to prototype filesystem paths
- define migration checkpoints that can be reviewed and rolled back
- keep architecture documents and implementation behavior synchronized

## Non-Goals

- keeping the old repository layout as a compatibility contract
- preserving YAML queue files as runtime truth
- moving generated dashboard pages into source repositories
- copying large generated artifacts into service or dashboard code
- building a full production system in one migration step

## Source Inventory

| Prototype Area | Examples | Migration Target | Treatment |
| --- | --- | --- | --- |
| Service/API scripts | `server.py`, `running_tasks.json` | `ttfhw-control-plane` | Rewrite around domain models and database state. |
| Batch orchestration | `batch-verify.py`, `verification-queue.yaml` | `ttfhw-control-plane`, `ttfhw-runner` | Split scheduling from execution. YAML becomes import/export only. |
| Runner prompts/skills | `.claude/skills/*`, executor scripts | `ttfhw-runner` | Port as explicit steps that consume `RunSpec`. |
| Data validation/migration | `scripts/validate_report.py`, `scripts/migrate-legacy.py` | `ttfhw-data-pipeline` | Rewrite into schema validators, fixtures, and migrations. |
| Verification reports | `json/` | `ttfhw-data-pipeline` or external archive | Import as immutable legacy snapshots. |
| Dashboard source | `app/`, `components/`, `lib/`, `static/` | `ttfhw-dashboard` | Rebuild as read-only frontend over published dashboard indexes. |
| Generated pages | `docs/` | deployment artifact | Do not treat as source of truth. |
| Repository inventory | `ttfhw.yml` | control-plane seed, data-pipeline manifest | Normalize and version. |
| Local workdirs | `repos/`, `work/`, `.cache/`, `venv/` | none | Runtime scratch only; do not migrate. |

## Migration Waves

### Wave 0: Governance Baseline

Owner: all repositories.

Actions:

- merge AI governance baseline in all repositories
- require `pre-commit run --all-files`
- require architecture consistency checks in PRs
- require implementation changes to update `computing-infra/TTFHW` docs or ADRs

Exit criteria:

- every repository has `AGENTS.md`, `specs/`, pre-commit, CI, and PR template
- local default pre-commit passes

### Wave 1: Contract Skeleton

Owner: `TTFHW`, `ttfhw-data-pipeline`, `ttfhw-control-plane`,
`ttfhw-runner`, `ttfhw-dashboard`.

Actions:

- formalize schemas for `RunSpec`, `StepResult`, `RunReport`,
  `DashboardIndex`, and `ArtifactRef`
- add JSON Schema or equivalent typed contracts in `ttfhw-data-pipeline`
- reference the schemas from repo-local specs
- add minimal valid fixtures for each payload

Exit criteria:

- schemas validate fixtures
- each implementation repository documents which contracts it reads or writes
- dashboard rejects unknown major contract versions by design

### Wave 2: Data Import And Normalization

Owner: `ttfhw-data-pipeline`.

Actions:

- import prototype `json/` as legacy fixtures
- classify split-format and legacy-format reports
- implement deterministic normalization into `RunReport`
- generate `DashboardIndex`
- redact internal paths, private IPs, and token-like values in publishable output

Exit criteria:

- current prototype report set can be normalized without the dashboard app
- golden fixtures cover representative success, failed, partial, skipped, and
  unknown cases
- generated dashboard index validates against schema

### Wave 3: Read-Only Dashboard

Owner: `ttfhw-dashboard`.

Actions:

- scaffold standalone frontend
- read only from generated dashboard index and report snapshots
- port summary, detail, filtering, sorting, and chart views
- remove backend mutation and queue assumptions

Exit criteria:

- dashboard builds against data-pipeline fixtures
- dashboard has no direct dependency on runner or control-plane internals
- smoke tests cover summary and detail pages

### Wave 4: Runner Extraction

Owner: `ttfhw-runner`.

Actions:

- implement CLI entrypoint that accepts `RunSpec`
- port verification steps as explicit, testable step modules
- emit raw `StepResult` payloads and artifact references
- add sandbox cleanup, timeout, and redaction behavior

Exit criteria:

- a single repository can run through a dry-run profile
- step outputs validate against data-pipeline schemas
- runner does not mutate control-plane state or dashboard files

### Wave 5: Control Plane Service

Owner: `ttfhw-control-plane`.

Actions:

- implement API around Repository, Job, Run, Step, Event, and ArtifactRef
- generate `RunSpec` from durable job state
- support runner polling or dispatch
- model cancel, retry, timeout, and audit events

Exit criteria:

- API can create and track jobs without YAML runtime state
- runner-facing payloads are versioned
- state transitions are covered by tests

### Wave 6: End-To-End Integration

Owner: all repositories.

Actions:

- control plane creates `RunSpec`
- runner executes and emits raw step output
- data pipeline normalizes and publishes snapshots
- dashboard renders published snapshots

Exit criteria:

- one batch can update the dashboard without modifying source repos
- each repository can be tested and deployed independently
- architecture docs match the implemented flow

## Forbidden Legacy Couplings

Do not reintroduce these prototype couplings:

- dashboard reading ad hoc prototype `json/` paths directly
- runner writing dashboard source or latest pointers
- control plane executing verification commands directly
- data pipeline scheduling jobs
- service runtime depending on generated `docs/` pages
- long-lived report history stored as primary control-plane database state
- credentials, local paths, or raw private logs published as dashboard data

## Architecture Consistency Requirement

Every migration PR must answer:

- which architecture document or ADR was consulted
- whether the migration changes repository boundaries or contracts
- whether `TTFHW` architecture docs or ADRs were updated
- which repo-local `specs/` were updated

Implementation that changes platform architecture without a synchronized doc or
ADR is a blocker.

## Review Order

Recommended review order:

1. `TTFHW` architecture and migration docs
2. `ttfhw-data-pipeline` contract and fixture changes
3. `ttfhw-dashboard` read-only data client and UI
4. `ttfhw-runner` execution steps
5. `ttfhw-control-plane` service orchestration
6. cross-repository integration changes
