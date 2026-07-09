# Review Workflow

## Purpose

Independent review prevents AI-generated work from being accepted merely because
it appears complete.

## Review Roles

Use these review lenses as applicable:

- architecture reviewer
- security reviewer
- contract/schema reviewer
- test/verification reviewer
- operations/deployment reviewer
- frontend UX reviewer for dashboard changes

## Review Steps

1. Read the self-check.
2. Read the architecture references.
3. Inspect the diff.
4. Verify repository boundary.
5. Check validation evidence.
6. List findings by severity.
7. Mark the result: approved, changes requested, or blocked.

## Severity

| Severity | Meaning |
| --- | --- |
| P0 | Must fix before merge; breaks architecture, data, security, or core behavior |
| P1 | Should fix before merge; likely defect or missing validation |
| P2 | Follow-up acceptable if tracked |
| P3 | Minor suggestion |

## Reviewer Independence

The same execution subject must not both implement and approve the change.

Low and medium risk changes may use an independent AI reviewer. High risk
changes require human confirmation after AI review.
