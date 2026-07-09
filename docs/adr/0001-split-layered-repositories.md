# ADR 0001: Split Implementation into Layered Repositories

## Status

Accepted

## Context

The prototype repository combines service code, runner logic, data archive,
dashboard source, and generated static pages. These assets have different
lifecycles and ownership boundaries.

## Decision

Split implementation into separate repositories:

- `ttfhw-control-plane`
- `ttfhw-runner`
- `ttfhw-data-pipeline`
- `ttfhw-dashboard`

Keep `computing-infra/TTFHW` as the architecture and governance repository.

## Consequences

Positive:

- clearer ownership
- independent deployment
- smaller blast radius
- data can be archived without polluting service code
- dashboard can evolve as a read-only frontend

Negative:

- more repositories to manage
- cross-repository contracts must be maintained
- initial migration cost is higher

## Follow-Up

Each implementation repository should link back to this repository as the
architecture authority.
