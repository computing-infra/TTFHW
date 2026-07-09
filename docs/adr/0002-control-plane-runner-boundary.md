# ADR 0002: Separate Control Plane from Runner Execution

## Status

Accepted

## Context

The control plane needs stable API semantics, durable state, retries, and audit
logs. The runner needs to execute untrusted code in changing environments such
as local Docker, remote SSH machines, and future Kubernetes workers.

Combining these concerns makes the service harder to secure and evolve.

## Decision

Keep the control plane and runner in separate repositories and runtime
processes.

The control plane emits immutable `RunSpec` payloads. The runner consumes
`RunSpec` and emits step results plus artifact references.

## Consequences

Positive:

- runner can change quickly without destabilizing the API
- execution hosts can be isolated from service hosts
- sandbox policy is easier to reason about
- future executor types can be added without rewriting the backend service

Negative:

- requires an explicit task dispatch or polling protocol
- more integration tests are needed

## Follow-Up

Define `RunSpec` and step result schemas in the data contract.
