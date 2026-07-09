# Architecture And Implementation Consistency

This document defines how TTFHW keeps architecture documents, repository specs,
and implementation behavior aligned.

## Principle

Architecture is not a one-time proposal. If implementation proves that an
architecture decision, boundary, data contract, or deployment assumption should
change, the architecture documents must be updated in the same change set or in
a linked prerequisite change.

Long-lived divergence between code and architecture is not allowed.

## Changes That Require Architecture Sync

Update the architecture repository when a change affects any of these areas:

- repository ownership or responsibility boundaries
- cross-repository APIs, payloads, schemas, or event contracts
- job, run, step, artifact, or report lifecycle semantics
- deployment topology, runtime model, or trust boundary
- security assumptions, sandboxing model, or credential handling
- data archive layout, retention policy, or dashboard-facing indexes
- compatibility or migration rules for public payloads

Small implementation details may stay in repo-local specs when they do not
change the platform-level contract.

## Required Update Path

Use the smallest sufficient update:

1. Update the relevant architecture document when the decision is already
   accepted and the document is stale.
2. Add or update an ADR when the change introduces a new platform decision or
   changes a previous decision.
3. Update repo-local `specs/` when the change only clarifies local behavior
   inside an existing boundary.

When in doubt, prefer an ADR plus a focused doc update.

## Pull Request Rule

Every implementation PR must answer:

- Does this change affect architecture, boundaries, contracts, deployment, or
  security assumptions?
- If yes, which `TTFHW` architecture document or ADR was updated?
- If no, why is this change implementation-local?

A PR that changes implementation behavior but leaves stale architecture
documents behind is not ready for merge.

## AI Agent Rule

AI agents must not silently encode new architecture in code.

When implementation reveals that architecture must change, the agent must:

1. stop broad implementation work,
2. identify the affected architecture source of truth,
3. update the architecture document or ADR,
4. update repo-local specs if needed,
5. continue implementation only after the intended architecture is explicit.

## Review Rule

Reviewers must check architecture consistency before approving:

- implementation stays inside the owning repository boundary
- cross-layer contracts match documented schemas
- deployment and security assumptions match architecture docs
- repo-local specs do not contradict `computing-infra/TTFHW`
- any intentional divergence is captured by an ADR
