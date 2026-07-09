# Quality Gates

## Gate 1: Local Hygiene

Required in every repository:

```bash
pre-commit run --all-files
```

The baseline checks should include:

- trailing whitespace
- end-of-file newline
- LF line endings
- YAML validity
- JSON validity
- TOML validity where applicable
- merge conflict markers
- added large files
- private key detection
- sensitive path denial
- gitleaks secret scanning
- detect-secrets baseline scanning
- GitHub Actions linting
- YAML linting

## Gate 2: Repository-Specific Validation

Add as soon as implementation code exists:

| Repository | Required validation |
| --- | --- |
| control plane | unit tests, API tests, DB migration checks |
| runner | unit tests, dry-run execution, cleanup behavior, shell/Docker/security scans |
| data pipeline | schema validation, fixture normalization, migration tests, redaction checks |
| dashboard | lint, typecheck, production build, Playwright smoke, public-env secret checks |

## Gate 3: Documentation Sync

When behavior changes, update the relevant spec or architecture document.
Architecture and implementation must be consistent before merge.

Required sync checks:

- cross-layer contract changed -> `TTFHW/docs/architecture/data-contract.md`
- repository boundary changed -> `TTFHW/docs/repo-map.md` or ADR
- deployment, trust boundary, or platform runtime changed ->
  `TTFHW/docs/architecture/deployment-topology.md` or ADR
- implementation revealed stale architecture ->
  `TTFHW/docs/architecture/implementation-consistency.md` plus the affected
  architecture document
- local workflow changed -> repo-local `specs/`
- AI process changed -> `TTFHW/spec/` and repo-local `AGENTS.md`

Block merge when code and architecture documents intentionally or accidentally
disagree and no ADR records the decision.

## Gate 4: Security

Before review:

- no secrets in code, docs, fixtures, logs, or examples
- no private keys
- no tokens printed in validation evidence
- destructive actions have explicit confirmation or dry-run behavior
- untrusted target repository execution is sandboxed
- no `.env`, credentials, token, or private-key files are committed
- dashboard `NEXT_PUBLIC_*` variables do not expose secret-like values
- verification reports are redacted before publication

## Gate 5: PR Evidence

Every PR should include:

- architecture references
- architecture impact decision
- architecture doc or ADR updates, when required
- changed files summary
- validation commands and results
- skipped checks and why
- risk level
- independent review result

## Docs-Only Changes

Docs-only changes may skip code tests, but still require:

- pre-commit
- source-of-truth check
- security check for accidental secrets
- self-check explaining why code tests were skipped
