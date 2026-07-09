# TTFHW

TTFHW (Time To First Hello World) is the architecture and governance repository
for the TTFHW verification platform.

This repository is the source of truth for platform boundaries, layered
architecture, data contracts, migration plans, and architecture decision records.
Implementation lives in separate repositories.

## Repository Map

| Repository | Responsibility |
| --- | --- |
| `computing-infra/TTFHW` | Architecture authority, ADRs, platform roadmap, contracts |
| `computing-infra/ttfhw-control-plane` | Backend control plane: APIs, jobs, scheduling, state, events |
| `computing-infra/ttfhw-runner` | Verification runner: sandbox execution, build/test steps, raw artifacts |
| `computing-infra/ttfhw-data-pipeline` | Schemas, validation, normalization, indexing, archive publishing |
| `computing-infra/ttfhw-dashboard` | Read-only dashboard and static deployment |

## Architecture Documents

- [Target Architecture](docs/architecture/target-architecture.md)
- [Layered Architecture](docs/architecture/layered-architecture.md)
- [Data Contract](docs/architecture/data-contract.md)
- [Deployment Topology](docs/architecture/deployment-topology.md)
- [Migration Plan](docs/architecture/migration-plan.md)
- [Repository Map](docs/repo-map.md)

## Architecture Decisions

- [ADR 0001: Split implementation into layered repositories](docs/adr/0001-split-layered-repositories.md)
- [ADR 0002: Separate control plane from runner execution](docs/adr/0002-control-plane-runner-boundary.md)
- [ADR 0003: Make verification data immutable and independently archived](docs/adr/0003-immutable-data-archive.md)
- [ADR 0004: Keep dashboard read-only and data-contract driven](docs/adr/0004-readonly-dashboard.md)

## Governance Rule

Implementation repositories should reference this repository for architecture
authority. Any change that crosses repository boundaries, changes data contracts,
or changes deployment topology should update the relevant document or ADR here
before implementation diverges.
