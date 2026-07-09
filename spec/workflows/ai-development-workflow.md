# AI Development Workflow

This workflow defines the standard closed loop for AI-assisted changes in TTFHW
repositories.

## States

Work should move through these states:

```text
intake
-> scoped
-> verified
-> planned
-> implemented
-> locally-validated
-> self-checked
-> independently-reviewed
-> ready-for-merge
```

Docs-only and architecture-only work may skip implementation-specific tests, but
must still provide evidence and a self-check.

## 1. Intake

Required:

- identify target repository
- identify owning layer
- read repo-local `AGENTS.md`
- read relevant architecture/spec documents
- confirm whether code changes are allowed

Forbidden:

- editing implementation files before understanding the repository boundary
- assuming prototype paths are future platform contracts

## 2. Scope

Required:

- state what layer owns the change
- state what layers must not be touched
- identify contract changes, if any
- identify architecture assumptions affected, if any
- decide whether an ADR is required

ADR required when:

- repository responsibility changes
- cross-layer payload changes incompatibly
- deployment topology changes
- security or trust boundary changes

## 3. Verify

Before implementation, verify the need or failure mode when possible:

- reproduce the bug, or
- inspect the existing contract gap, or
- confirm the missing spec, or
- explain why verification is not possible yet

Evidence should include commands, file references, or concrete observations.

## 4. Plan

Required:

- identify files or specs to change
- identify validation commands
- identify risks and rollback path
- keep plan within repository boundary

## 5. Implement

Rules:

- keep changes scoped
- prefer contracts and tests before broad implementation
- do not mix unrelated cleanup
- do not commit generated artifacts unless explicitly required
- do not bypass schema validation for cross-layer data
- do not encode new architecture only in code
- when implementation changes an architecture assumption, update the relevant
  architecture document or ADR before continuing broad implementation

## 6. Local Validation

Minimum:

```bash
pre-commit run --all-files
```

Repository-specific validation must be added once code exists:

- control plane: unit tests, API tests, migration tests
- runner: dry-run tests, executor tests, sandbox cleanup tests
- data pipeline: schema tests, fixture tests, migration tests
- dashboard: lint, typecheck, build, Playwright smoke tests

If validation cannot be run, record the exact blocker.

## 7. Self-Check

Use `docs/ai-templates/pr-self-check.md` as the author self-check format.

Must include:

- actor identity
- scope
- architecture references
- architecture impact decision and any required doc or ADR update
- tests run
- risks
- skipped checks and reasons

## 8. Independent Review

Author and reviewer must be different execution subjects. A second AI agent can
serve as reviewer for low/medium-risk changes; high-risk changes require human
final confirmation.

Review must check:

- architecture boundary
- contract compatibility
- security
- tests
- documentation sync

Use `docs/ai-templates/review-report.md`.

## 9. Ready For Merge

A change is ready only when:

- local checks pass or documented skips are acceptable
- CI passes or failure is proven unrelated
- self-check exists
- independent review exists
- architecture/spec docs are synchronized
- implementation and architecture are consistent
- no blocker remains

## Blockers

Default blockers:

- cross-repository contract changed without architecture update
- implementation behavior changes platform architecture without an updated doc
  or ADR
- missing schema version for public payload
- runner executes unsandboxed untrusted code without explicit design approval
- dashboard mutates job state
- control plane stores full historical reports as primary archive
- secrets or credentials appear in examples, logs, tests, or docs
- author self-check is presented as independent review
