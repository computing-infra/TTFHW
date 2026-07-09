# Migration Plan

Detailed repository migration waves and acceptance criteria are maintained in
`docs/migration/repository-migration-plan.md`.

## Current Source

The current prototype repository is `kerer-ai/ttfhw-verify-batch`.

It contains:

- backend scripts
- runner-like scripts
- Claude skills
- normalized and legacy JSON reports
- Next.js dashboard source
- generated `docs/` pages
- queue YAML

The migration should treat that repository as a source of historical assets, not
as the target structure.

## Phase 0: Freeze Architecture Direction

Actions:

- Keep architecture authority in `computing-infra/TTFHW`.
- Use ADRs for cross-boundary decisions.
- Avoid adding new platform responsibilities to the prototype repository.

Exit criteria:

- Implementation repositories link back to this architecture repository.

## Phase 1: Extract Data Contracts

Target repository:

- `computing-infra/ttfhw-data-pipeline`

Actions:

- define `RunSpec`, step result, normalized report, dashboard index schemas
- migrate current split-format and legacy-format JSON into normalized reports
- generate `latest/index.json` and `latest/repos/*.json`
- add validators and golden fixtures

Exit criteria:

- dashboard-ready data can be generated without running the old Next.js app
- current 59 repositories can be represented by the new report schema

## Phase 2: Extract Dashboard

Target repository:

- `computing-infra/ttfhw-dashboard`

Actions:

- create standalone Next.js app
- read data from `DATA_BASE_URL` or local `public/data`
- port summary and detail views
- remove backend task controls from dashboard scope
- add Playwright smoke tests

Exit criteria:

- dashboard builds from data-pipeline output
- dashboard repository contains no verification runner or queue state

## Phase 3: Extract Runner

Target repository:

- `computing-infra/ttfhw-runner`

Actions:

- define CLI that accepts `RunSpec`
- implement local Docker executor
- implement remote SSH executor if still required
- port verification skills or step prompts
- emit step-level JSON and artifact references

Exit criteria:

- a single repository can be verified by invoking runner with a RunSpec
- outputs validate against data-pipeline schemas

## Phase 4: Build Control Plane

Target repository:

- `computing-infra/ttfhw-control-plane`

Actions:

- build FastAPI service
- model Repository, Job, Run, Step, Event
- implement job submission, status, cancel, retry
- support runner polling or dispatch
- persist state in PostgreSQL

Exit criteria:

- jobs can be submitted through API
- runners can consume tasks
- YAML queue is no longer runtime source of truth

## Phase 5: End-to-End Integration

Actions:

- control plane creates RunSpec
- runner executes and writes raw outputs
- data pipeline publishes normalized snapshots
- dashboard reads latest snapshot

Exit criteria:

- one full verification batch updates dashboard without modifying source repos
- each repository can be deployed and tested independently

## Legacy Path Mapping

| Prototype Path | Future Home |
| --- | --- |
| `server.py` | `ttfhw-control-plane`, rewritten as modular FastAPI |
| `batch-verify.py` | split between `ttfhw-control-plane` and `ttfhw-runner` |
| `.claude/skills/*` | `ttfhw-runner`; schemas/templates may move to `ttfhw-data-pipeline` |
| `scripts/validate_report.py` | `ttfhw-data-pipeline` |
| `scripts/migrate-legacy.py` | `ttfhw-data-pipeline` |
| `app/`, `components/` | `ttfhw-dashboard` |
| `lib/data-loader.ts` | rewritten as dashboard data client |
| `json/` | data archive |
| `docs/` | generated deployment output, not source of service truth |
| `verification-queue.yaml` | import/export only; runtime state moves to database |
| `ttfhw.yml` | inventory seed or dedicated config source |
