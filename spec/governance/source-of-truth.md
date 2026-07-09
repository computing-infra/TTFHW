# Source of Truth Matrix

| Information | Source of Truth |
| --- | --- |
| Platform architecture | `TTFHW/docs/architecture/*` |
| Architecture and implementation consistency | `TTFHW/docs/architecture/implementation-consistency.md` |
| Accepted architecture decisions | `TTFHW/docs/adr/*` |
| Repository responsibilities | `TTFHW/docs/repo-map.md` |
| Cross-layer payloads | `TTFHW/docs/architecture/data-contract.md` |
| AI development workflow | `TTFHW/spec/workflows/ai-development-workflow.md` |
| Quality gates | `TTFHW/spec/foundations/quality-gates.md` |
| Repo-local non-goals | implementation repo `specs/architecture-boundary.md` |
| Current code behavior | implementation repository code and tests |
| CI status | GitHub Actions run result |
| Generated reports | data archive snapshot |

## Conflict Handling

If facts conflict:

1. Prefer accepted ADRs for architectural intent.
2. Prefer code/tests for current implementation behavior.
3. Prefer data archive snapshots for published verification history.
4. Update stale docs rather than relying on stale assumptions.

If implementation needs to contradict architecture, stop and create or update an
ADR first.

If implementation reveals that existing architecture docs are stale rather than
wrong in principle, update the affected architecture document in the same change
set or link to the prerequisite architecture update.
