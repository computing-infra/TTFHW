# Layered Architecture

## 1. Control Plane

The control plane is the stable backend service layer.

### Responsibilities

- repository inventory ingestion
- verification profile management
- job submission
- run lifecycle state
- retries, cancellation, and timeout policy
- runner dispatch or worker polling
- event stream
- audit log
- API authentication and authorization

### Recommended Stack

- Python 3.12+
- FastAPI
- Pydantic v2
- PostgreSQL
- SQLAlchemy 2.x or SQLModel
- Alembic
- OpenTelemetry
- pytest

### Internal Modules

```text
app/
  api/
  domain/
  db/
  services/
  events/
  settings.py
  main.py
```

### Boundary

The control plane produces `RunSpec` and consumes status/events. It does not
compile repositories or store long-lived report JSON.

## 2. Runner

The runner is the execution layer.

### Responsibilities

- clone target repository
- prepare sandbox
- execute verification steps
- collect logs and artifacts
- emit step-level results
- clean up temporary resources

### Recommended Stack

- Python CLI
- Typer or Click
- Pydantic v2
- Docker/Podman integration
- remote SSH executor
- future Kubernetes executor
- structured JSON logs

### Executor Types

```text
local-docker
remote-ssh
kubernetes
```

### Boundary

The runner receives an immutable `RunSpec` and writes raw step results. It does
not mutate dashboard files or own the authoritative job state.

## 3. Data Pipeline

The data pipeline owns schema, validation, normalization, indexing, and
publishing.

### Responsibilities

- canonical schema definitions
- backward-compatible migrations
- report normalization
- data quality checks
- dashboard index generation
- latest snapshot generation
- analytical export generation

### Recommended Stack

- Python
- Pydantic v2 or JSON Schema
- DuckDB
- Parquet
- pytest with golden fixtures

### Boundary

The data pipeline consumes runner artifacts and publishes validated report
snapshots. It does not schedule verification jobs.

## 4. Dashboard

The dashboard is the read-only presentation layer.

### Responsibilities

- summary page
- repository detail page
- filtering and sorting
- charts
- batch comparison
- trend views
- static deployment

### Recommended Stack

- Next.js
- TypeScript
- TanStack Table
- Recharts or ECharts
- Zod or generated TypeScript contracts
- Playwright for smoke and visual checks

### Boundary

The dashboard reads published index/report data. It does not mutate queues or
call runners directly.

## 5. Archive

The archive is the durable data layer for published verification outputs.

### Storage Options

Stage 1:

- Git data repository for small JSON indexes and reports

Stage 2:

- object storage for artifacts and full history
- Parquet datasets for analytics

### Layout

```text
runs/
  <run_id>/
    manifest.json
    repos/
      <repo>/
        steps/
        report.json
        artifacts/
latest/
  manifest.json
  index.json
  repos/
datasets/
  reports.parquet
  steps.parquet
```

## 6. Dependency Rules

- Control plane can reference schema packages, but not dashboard source.
- Runner can reference run-spec and step schemas.
- Data pipeline can reference all data schemas, but not service internals.
- Dashboard can reference published dashboard contracts only.
- No layer may depend on generated files from a downstream layer.
