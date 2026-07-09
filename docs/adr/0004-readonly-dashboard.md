# ADR 0004: Keep Dashboard Read-Only and Data-Contract Driven

## Status

Accepted

## Context

The prototype combines dashboard display with task-management concerns through
a local backend. This is convenient, but it makes deployment and ownership
unclear.

## Decision

The dashboard is a read-only frontend. It consumes dashboard indexes and report
snapshots produced by the data pipeline. It does not mutate queues, trigger
runners, or own control-plane state.

Operator controls, if needed, should live in a separate operator UI or call the
control-plane API explicitly.

## Consequences

Positive:

- dashboard can be statically deployed
- public/internal read-only views are safer
- frontend can evolve independently
- data contracts become the integration point

Negative:

- task control UI requires a separate surface or authenticated control-plane UI
- dashboard cannot rely on local backend files

## Follow-Up

Build dashboard data clients against `ttfhw.dashboard_index.v1` and
`ttfhw.report.v1`.
