# PR Self-Check Template

## Actor

- Author:
- Repository:
- Branch:

## Summary

## Architecture References

- Architecture doc:
- ADR:
- Repo-local spec:
- Architecture impact:
- Architecture docs/ADR updated:

## Boundary Check

- [ ] Change stays within repository ownership.
- [ ] Cross-layer contracts are unchanged or architecture docs were updated.
- [ ] Architecture assumptions, deployment topology, trust boundaries, and data
      contracts are unchanged or `computing-infra/TTFHW` was updated.
- [ ] Implementation behavior and architecture documents are consistent.
- [ ] Generated artifacts are not committed unintentionally.

## Validation

```text
commands and results
```

## Security Check

- [ ] No secrets, tokens, private keys, or sensitive internal data.
- [ ] Destructive actions are guarded or not applicable.
- [ ] Untrusted execution boundary is respected or not applicable.

## Risk Level

- `low` / `medium` / `high`

Reason:

## Skipped Checks

## Residual Risks
