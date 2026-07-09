# ADR 0003: Make Verification Data Immutable and Independently Archived

## Status

Accepted

## Context

The prototype stores report JSON and generated pages in the same repository as
the service and dashboard source. This makes history hard to manage and causes
service changes to be mixed with data churn.

## Decision

Verification outputs are published as immutable run snapshots. The data archive
is independent from service source code. `latest` is a generated view over
immutable runs, not the source of historical truth.

## Consequences

Positive:

- historical runs are reproducible
- dashboard can read immutable snapshots
- data retention and cleanup can be handled separately
- service repositories remain small

Negative:

- archive publishing must be explicit
- storage layout and schema versioning must be governed

## Follow-Up

Implement validators, normalizers, and index generation in
`ttfhw-data-pipeline`.
