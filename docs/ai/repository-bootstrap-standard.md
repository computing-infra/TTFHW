# Repository Bootstrap Standard

New TTFHW implementation repositories should start with the following structure.

```text
AGENTS.md
README.md
specs/
  README.md
  architecture-boundary.md
.codex/
  skills/
    <repo-skill>/
      SKILL.md
.github/
  workflows/
    ci.yml
  pull_request_template.md
.pre-commit-config.yaml
```

## `AGENTS.md`

Purpose:

- tell AI agents how to work in this repository
- link back to architecture authority
- define local validation commands
- list hard non-goals

## `specs/`

Purpose:

- describe local contracts before code exists
- capture acceptance criteria
- define ownership boundaries
- provide stable references for future implementation PRs

## `.codex/skills/`

Purpose:

- provide compact repo-specific workflows
- guide AI agents through predictable implementation and review steps
- keep repeated project knowledge out of ad hoc prompts

## `.pre-commit-config.yaml`

Purpose:

- catch formatting, YAML, JSON, whitespace, and syntax issues locally
- add language-specific hooks only when the repository introduces that language

## GitHub Workflow

The initial workflow may be lightweight. It should at least run pre-commit on
all files. As soon as code is introduced, repository-specific tests must be
added to CI.
