# TTFHW Specification Entry

`spec/` is the formal rule source for AI-assisted development across TTFHW
repositories. Entry documents such as `README.md`, `AGENTS.md`, and repo-local
skills may route agents here, but they must not weaken these rules.

## Minimum Reading Set

Before any implementation work:

1. `docs/architecture/target-architecture.md`
2. `docs/repo-map.md`
3. `spec/workflows/ai-development-workflow.md`
4. `spec/foundations/quality-gates.md`
5. `spec/governance/source-of-truth.md`

## Task Routing

| Task | Read |
| --- | --- |
| Cross-repository design | `docs/architecture/*`, `docs/adr/*` |
| Implementation planning | `spec/workflows/ai-development-workflow.md` |
| PR readiness | `spec/foundations/quality-gates.md`, `docs/ai-templates/pr-self-check.md` |
| Independent review | `spec/workflows/review-workflow.md`, `docs/ai-templates/review-report.md` |
| Contract changes | `docs/architecture/data-contract.md`, ADRs |
| Repo boundary questions | `docs/repo-map.md`, repo-local `specs/architecture-boundary.md` |

## Authority Rule

When documents conflict:

1. Accepted ADRs
2. `docs/architecture/*`
3. `spec/*`
4. repo-local `specs/*`
5. `AGENTS.md` and skills
6. README and informal notes

Implementation must stop and update the higher-authority document when a lower
document cannot be reconciled.
