# Data Contract

## Contract Principles

- Every cross-layer payload must include `schema_version`.
- Runner outputs are factual step records, not presentation objects.
- Data pipeline output is immutable once published under a run ID.
- `latest` is a generated pointer or snapshot, not historical truth.
- Large logs and binary artifacts are referenced, not embedded.

## RunSpec

`RunSpec` is emitted by the control plane and consumed by the runner.

```json
{
  "schema_version": "ttfhw.run_spec.v1",
  "run_id": "run_20260709_000001",
  "repository": {
    "name": "ubs-engine",
    "url": "https://gitcode.com/openeuler/ubs-engine.git",
    "ref": "master"
  },
  "profile": {
    "steps": ["doc_scan", "static_check", "build", "test"],
    "timeout_seconds": 14400,
    "build_ratio": 20
  },
  "execution": {
    "executor": "local-docker",
    "image": "openeuler/openeuler:latest"
  },
  "output": {
    "artifact_base": "s3://ttfhw-runs/run_20260709_000001/"
  }
}
```

## Step Result

Each runner step writes one step result.

```json
{
  "schema_version": "ttfhw.step.build.v1",
  "run_id": "run_20260709_000001",
  "repo": "ubs-engine",
  "step": "build",
  "status": "success",
  "started_at": "2026-07-09T12:00:00Z",
  "completed_at": "2026-07-09T12:15:00Z",
  "duration_seconds": 900,
  "commands": [
    {
      "command": "cmake -S . -B build",
      "exit_code": 0,
      "duration_seconds": 120,
      "log_ref": {
        "uri": "s3://ttfhw-runs/run_20260709_000001/repos/ubs-engine/artifacts/cmake.log",
        "sha256": "..."
      }
    }
  ],
  "artifacts": []
}
```

## Normalized Report

The data pipeline produces one normalized report per repository per run.

```json
{
  "schema_version": "ttfhw.report.v1",
  "run_id": "run_20260709_000001",
  "repo": {
    "name": "ubs-engine",
    "url": "https://gitcode.com/openeuler/ubs-engine.git",
    "ref": "master",
    "group": "UBSCore"
  },
  "result": {
    "overall": "success",
    "build": "success",
    "test": "partial_success",
    "sample": "not_run"
  },
  "duration_seconds": 6000,
  "steps": {
    "doc_scan": "success",
    "static_check": "success",
    "build": "success",
    "test": "partial_success"
  },
  "artifact_refs": []
}
```

## Dashboard Index

The dashboard reads this index as its primary entry point.

```json
{
  "schema_version": "ttfhw.dashboard_index.v1",
  "generated_at": "2026-07-09T12:00:00Z",
  "run_id": "run_20260709_000001",
  "summary": {
    "total": 59,
    "success": 20,
    "failed": 5,
    "partial_success": 34
  },
  "repos": [
    {
      "name": "ubs-engine",
      "group": "UBSCore",
      "result": "success",
      "build_status": "success",
      "test_status": "partial_success",
      "duration_seconds": 6000,
      "report_url": "repos/ubs-engine.json"
    }
  ]
}
```

## Status Vocabulary

Canonical result values:

```text
success
failed
partial_success
not_run
skipped
unknown
```

Runner step status may additionally include:

```text
pending
running
cancelled
timeout
```

## Versioning Rules

- Adding optional fields is backward compatible.
- Removing fields or changing meaning requires a new major contract version.
- The data pipeline owns migrations from older versions.
- Dashboard should reject unknown major versions by default.

## Artifact Reference

```json
{
  "type": "log",
  "name": "build.log",
  "uri": "s3://ttfhw-runs/run_id/repos/ubs-engine/artifacts/build.log",
  "sha256": "...",
  "content_type": "text/plain"
}
```

Artifacts should be content-addressed or checksum-verified when possible.
