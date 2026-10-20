# Handover Package Template

Trim each section to the project; delete rows that do not apply; do not leave placeholders. Bracketed text is guidance.

中文版：[handover-template.zh-CN.md](handover-template.zh-CN.md)

## File 1: HANDOVER.md

```markdown
# HANDOVER — [Project name]

> Handover time: [YYYY-MM-DD HH:mm]
> Reason: [context length / direction change / milestone / agent switch / other]
> Current phase: [phase]
> Start here: read section 0, then section 10.

## 0. At a glance

- Goal in one sentence: [final deliverable]
- Current state: [where the project stands]
- Next action: [the first thing to do]
- Biggest risk / blocker: [write "none" if none]
- Reading order: [e.g. 0 → 10 → 3 → 4]

## 1. Goal and scope

### Final deliverable

- [artifact, format, audience]

### Acceptance criteria

- [ ] [observable or numeric criterion]

### Explicitly out of scope

- [prevents the next agent from expanding scope]

## 2. Phase and progress

| Milestone | Status | Evidence | Notes |
|---|---|---|---|
| [name] | Done / In progress / Not started / Blocked / Abandoned | [path, command output, commit] | |

| Work item | Status | Evidence | Dependency / owner |
|---|---|---|---|
| [item] | | | |

## 3. Decision log

| Date | Decision | Why | Alternatives rejected | Cost / constraint |
|---|---|---|---|---|
| | | | | |

Record only decisions that affect later choices; skip the chronological log.

## 4. Dead ends and negative constraints

| Do not retry | Why it failed | Evidence | Revisit when |
|---|---|---|---|
| [approach X] | [performance / deadlock / no permission] | [log, experiment, commit] | [condition, or "never"] |

## 5. Artifact map

| Path | Purpose | State | Authoritative? | Notes |
|---|---|---|---|---|
| [path] | [one sentence] | Complete / Draft / Stale | Yes / No | [why this is the trusted version] |

"Authoritative" means the version a new agent should trust when several exist.

## 6. Environment and commands

- OS / hardware: []
- Runtime and versions: []
- Dependency installation: [command]
- Start: [command]
- Build: [command]
- Test / lint: [command, latest result]
- External services and permissions: [service; where credentials live, not their values]
- Config files: [path and purpose]
- Known environment traps: []

## 7. Data, parameters, and external state

- Data / models / inputs and outputs: [path, version, size]
- Key parameters: []
- Branch / uncommitted changes / stashes: []
- External systems: [deployed version, queues, remote divergence]
- Long-running or scheduled jobs: [what is running, how to check]

## 8. Known issues and risks

| Issue | Impact | Evidence | Workaround | Recommended action |
|---|---|---|---|---|
| | | | | |

## 9. Assumptions and inconsistencies

| Item | Source A | Source B | Evidence | Who can confirm |
|---|---|---|---|---|
| [assumption or conflict] | [conversation/file/git] | [conversation/file/git] | | |

## 10. Next steps

### P0 — Do now

- Action: [specific file and operation]
- Output: []
- Definition of done: []
- Dependency / risk: []

### P1 — Do next

- [same format]

### Do not start with

- [related-looking work that would derail the main line]

## 11. Handover notes

- User preferences / prohibitions: []
- Communication and output format requirements: []
- Decisions that need a human: []

## 12. Changes since the last handover

Write "None" for the first handover. Otherwise:

- Added: []
- Changed: []
- No longer valid: []

## 13. Acceptance checks

- [ ] Can restate the goal and acceptance criteria
- [ ] Can point to the current state and its evidence
- [ ] Can name at least two dead ends
- [ ] Can execute the first P0 action
- [ ] Knows which questions require a human

## 14. Evidence index

- Key commands: []
- Log locations: []
- Key conversation points: [turn/topic]
- External links: []
```

## File 2: SYSTEM_PROMPT_NEXT.md

```markdown
# Handover prompt — [Project name]

You are taking over [Project name]. Your task is [one-sentence goal].

Before acting, read `[absolute path to HANDOVER.md]`. If you cannot read it, proceed with the information below and tell the user that the detailed handover package is missing.

## Goal and acceptance

- Goal: []
- Definition of done: []
- Out of scope: []

## Hard constraints

- [requirements, interfaces, or formats that must not change]
- [questions that require a human]

## Current state (as of [date])

- Phase: []
- Done: []
- In progress: []
- Blocked: []

## Abandoned paths (do not retry)

- [approach X: reason]

## First action

1. [first file or command to inspect]
2. [first real action]

## Working rules

- Check files and git state before acting; if they contradict HANDOVER.md, report it before proceeding.
- Make the smallest change that advances the goal; do not refactor unrelated code.
- Collect decisions that need a human into one set of questions; do not assume.
- Never print or commit secrets.
```
