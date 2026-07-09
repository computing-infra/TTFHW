# AI Engineering Standards

This document defines how AI agents should work across TTFHW repositories.

## Required Working Pattern

1. Read this repository's architecture documents before making cross-boundary changes.
2. Read the target repository's `AGENTS.md` before editing files.
3. Check `specs/` for the active contract and non-goals.
4. Keep implementation inside the repository's ownership boundary.
5. Add or update tests and validation when changing behavior.
6. Run local checks before proposing a commit.
7. Summarize verification results and known gaps.

## Architecture Authority

The source of truth is `computing-infra/TTFHW`.

Implementation repositories may add local details, but they must not contradict:

- `docs/architecture/target-architecture.md`
- `docs/architecture/layered-architecture.md`
- `docs/architecture/data-contract.md`
- `docs/architecture/implementation-consistency.md`
- `docs/repo-map.md`
- accepted ADRs under `docs/adr/`

If implementation proves that architecture, boundaries, contracts, deployment,
or security assumptions must change, update the architecture document or ADR in
the same change set or in a linked prerequisite change. Do not leave new
architecture encoded only in implementation code.

## AI Delivery Guardrails

- Do not use the old prototype filesystem layout as a platform contract.
- Do not move responsibilities across repository boundaries without an ADR.
- Do not let Dashboard code mutate verification jobs or queues.
- Do not let Runner code own authoritative job state.
- Do not let Control Plane code store full historical report archives.
- Do not embed large logs or binary artifacts in JSON reports.
- Do not bypass schema validation when producing cross-layer data.

## Quality Gates

Every repository should provide:

- `AGENTS.md` for agent-specific local instructions
- `specs/` for active contracts and boundaries
- `.codex/skills/` for reusable AI workflows
- `.pre-commit-config.yaml` for local checks
- `.github/workflows/ci.yml` for baseline CI
- `.github/pull_request_template.md` for review discipline

## Pull Request Expectations

PRs should state:

- architecture document or ADR consulted
- whether implementation changed architecture assumptions
- architecture document or ADR updated, when required
- repository boundary affected
- user-visible behavior change
- validation commands run
- known residual risks

## Escalation Rule

If an implementation requires changing cross-repository contracts, first update
the architecture repository with either:

- a focused spec change, or
- a new ADR.

The same rule applies to repository boundaries, deployment topology, trust
boundaries, security assumptions, and public data contracts.
