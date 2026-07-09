# Repository Map

This document defines the intended ownership boundary for each TTFHW repository.

## Architecture Authority

### `computing-infra/TTFHW`

Owns:

- platform architecture
- repository boundaries
- ADRs
- data contract policy
- migration plan
- platform roadmap

Does not own:

- production service implementation
- runner implementation
- verification report archive
- dashboard build artifacts

## Implementation Repositories

### `computing-infra/ttfhw-control-plane`

Owns:

- API service
- job and run lifecycle
- repository inventory ingestion
- scheduler and retry policy
- event stream
- operator-facing backend state
- database migrations

Does not own:

- compiling target repositories
- long-term report archive
- dashboard UI
- generated static site assets

### `computing-infra/ttfhw-runner`

Owns:

- repository checkout
- sandbox setup
- local Docker / remote SSH / future Kubernetes executors
- document scan, static check, build, test, sample steps
- raw step results
- raw logs and artifacts
- execution cleanup

Does not own:

- authoritative job state
- historical archive layout
- dashboard rendering
- user-facing API

### `computing-infra/ttfhw-data-pipeline`

Owns:

- canonical schemas
- validators
- normalizers
- legacy migrations
- run manifest generation
- dashboard index generation
- latest snapshot publishing
- Parquet or analytical exports

Does not own:

- task scheduling
- sandbox execution
- dashboard UI

### `computing-infra/ttfhw-dashboard`

Owns:

- summary and detail report UI
- filtering, sorting, charting
- static frontend deployment
- typed data adapters for dashboard indexes

Does not own:

- verification execution
- queue mutation
- control-plane state
- long-term report authority

## Cross-Repository Dependency Direction

Allowed dependency direction:

```text
TTFHW architecture docs
  -> control-plane
  -> runner
  -> data-pipeline
  -> dashboard
```

Runtime data flow:

```text
control-plane -> runner -> data-pipeline -> archive -> dashboard
```

Dashboard must not call runner directly. Runner must not write dashboard source
files. Data pipeline must not own job scheduling. Control plane must not embed
long-lived report history.
