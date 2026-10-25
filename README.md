# project-handover

[English](README.md) | [简体中文](README.zh-CN.md)

![Validate skill](https://github.com/NormanGOING/project-handover/actions/workflows/validate.yml/badge.svg)

> Hand over the project, not the chat.

`project-handover` produces a complete handover package for a fresh AI agent: goals, current state, decisions, dead ends, artifacts, environment, and next steps. It inspects the conversation, project files, git state, and environment, then writes `HANDOVER.md` plus `SYSTEM_PROMPT_NEXT.md`.

## What you get

- `HANDOVER.md`: goal, progress, decisions, dead ends, artifact map, environment, risks, and next steps — each backed by evidence where possible.
- `SYSTEM_PROMPT_NEXT.md`: a ready-to-paste opening prompt with hard constraints, state summary, first action, and definition of done.

## Why

Long conversations drift. Common failures:

- The goal moves and the next agent does not know what is actually being delivered.
- Old attempts pollute the context and failed paths get retried.
- Conclusions stay in the chat and disappear with the session.
- The handover says what was discussed but not what the project actually is now.

This skill inspects the conversation, project files, git state, configuration, and test results before writing. When sources conflict, it does not guess; it records both claims under "Inconsistencies".

## Install

### One command (recommended)

```bash
npx skills@latest add NormanGOING/project-handover
```

This installs the skill through the [skills.sh](https://skills.sh) CLI.

### Codex

```bash
git clone https://github.com/NormanGOING/project-handover.git ~/.codex/skills/project-handover
```

Windows PowerShell:

```powershell
git clone https://github.com/NormanGOING/project-handover.git "$env:USERPROFILE\.codex\skills\project-handover"
```

### Claude Code

`SKILL.md` uses the same format. Install it with:

```bash
git clone https://github.com/NormanGOING/project-handover.git ~/.claude/skills/project-handover
```

Or copy it into a project's `.claude/skills/` directory.

### Other agents

Give the agent `SKILL.md` and `references/`, or reference `SKILL.md` from custom instructions. The workflow does not depend on Codex-specific APIs; `agents/openai.yaml` only provides Codex UI metadata.

## Usage

Say:

- "Use project-handover to hand this project off."
- "The context is getting long. Reset it and generate a handover package."
- "Do a milestone summary; the next agent will take over."

You can also invoke `$project-handover` explicitly.

Default output:

```text
<project-root>/handover/<YYYY-MM-DD-HHmm>/
├── HANDOVER.md
└── SYSTEM_PROMPT_NEXT.md
```

Each run creates a new timestamped directory. Older handovers are never overwritten.

## What it inspects

| Source | Content |
|---|---|
| Conversation | Goals, user corrections, rejected approaches, promises, open questions |
| Files | Directory structure, docs, configuration, dependencies, tests, scripts, logs |
| Git | Branch, HEAD, uncommitted and untracked files, stashes, remote divergence |
| Environment | Runtime, installation method, external services, hardware, key paths |
| Runtime state | Test, build, and lint commands with their latest results |

## Safety

- Read-only by default: no code edits, file moves, commits, branch switches, stashes, or resets.
- No secret values: only variable names, config locations, and how to obtain them.
- No overwriting or deleting older handovers.
- If the project structure needs changes, it proposes a migration list and waits for per-item approval.

## Example output (excerpt)

```markdown
## 0. At a glance

- Goal in one sentence: deliver an in-memory Todo API that uses only the Python standard library.
- Current state: add/list are implemented and tested; complete is written but uncommitted and untested.
- Next action: confirm the index convention, test `complete`, then add HTTP routes.
- Biggest risk: the README promises an "API", but the repository has no HTTP entry point.
```

```markdown
## 4. Dead ends and negative constraints

| Do not retry | Why it failed | Evidence | Revisit when |
|---|---|---|---|
| SQLite persistence | Writes fail with `unable to open database file` | `DECISIONS.md` | The deployment environment provides a writable directory |
| Flask | The deployment machine cannot install third-party packages | `README.md` | The deployment constraint changes |
```

Full structure: [`references/handover-template.md`](references/handover-template.md).

## Design principles

1. **Inspect before asking.** Facts available from files, git, and logs are not questions for the user.
2. **Separate facts from intent.** Files and git define current state; the conversation defines goals and trade-offs. Conflicts are recorded explicitly.
3. **Complete coverage, cited not copied.** Artifacts get a path and one-line purpose; old documents are not pasted again.
4. **Dead ends stay dead.** State what not to retry and why, so the next agent does not repeat the same failure.
5. **Executable next steps.** Every next step has an action, an output, and a definition of done.

## Task types

[`references/domain-checklists.md`](references/domain-checklists.md) adds checks for:

- Code / architecture
- Research / experiments
- Multi-agent / workflows
- Long-form writing / scripts / planning
- Operations / deployment

Only the relevant section is loaded.

## Languages

The skill instructions are English-primary. Chinese translations are included:

- [SKILL.zh-CN.md](SKILL.zh-CN.md)
- [Handover template](references/handover-template.zh-CN.md)
- [Domain checklists](references/domain-checklists.zh-CN.md)

## Limitations

- It can only hand over information that is recorded or discoverable in the project. Context that exists only in someone's head must be supplied by the user.
- Very large repositories should be handed over module by module rather than listing every file at once.
- Review the generated prompt before giving it to a new agent.

## Validation

Run `python scripts/validate.py` before opening a PR. CI runs the same check on every push.

## Contributing

Issues and pull requests are welcome. One rule: **add decision criteria, not more fixed steps.**

## License

MIT
