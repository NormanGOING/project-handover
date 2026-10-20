---
name: project-handover
description: "Create a complete, resumable project handover package (HANDOVER.md + SYSTEM_PROMPT_NEXT.md) when switching conversations or agents, when context is too long or polluted, or at a milestone wrap-up (交接, 上下文重置, 阶段性总结). Covers goals, state, decisions, dead ends, artifacts, environment, risks, and next steps; also maps an existing project for a fresh agent. Use a lighter handoff flow when only a short conversation summary is needed."
---

# Project Handover

Produce a handover package that lets a fresh agent with no memory of this conversation continue the work. Transfer executable state, not a chat transcript. Write in the user's language, falling back to English when the user's language is unclear.

中文版：[SKILL.zh-CN.md](SKILL.zh-CN.md)

## Three rules

1. **Inspect before asking.** Never ask the user for a fact you can find in files, git, configuration, logs, or dependency manifests.
2. **Separate facts from intent.** Files and git are authoritative for current state; the conversation is authoritative for goals, constraints, and trade-offs. When they conflict, do not silently pick one. Record both claims and the evidence under "Inconsistencies".
3. **Read-only by default.** Do not edit code, move or rename files, commit, switch branches, stash, reset, clean, or start long-running jobs. If the project needs restructuring, propose a migration list and wait for explicit per-item approval.

## Workflow

### 1. Locate the project and output directory

- Find the project root: the git root, a directory the user named, or the current working directory.
- Write to `<project-root>/handover/<YYYY-MM-DD-HHmm>/` by default. If the name exists, append `-2`, `-3`, and so on. Never overwrite.
- If you are not in a project or the boundary is unclear, ask where to write the package and what is in scope.

### 2. Collect facts in parallel

- **Conversation**: goals, explicit user requirements, corrections, rejected approaches, promises, open questions, and the latest conclusions. If the runtime exposes thread or session reading tools, use them to recover earlier context.
- **Files**: directory structure, README, docs, configuration, dependency manifests, tests, scripts, data, assets, and logs. For large repositories, group by module instead of listing every file.
- **Git**: branch, HEAD, status (including untracked files), recent commits, divergence from the remote, and stashes.
- **Environment**: runtime and versions, installation method, external services, hardware, and key paths.
- **Runtime state**: run only read-only or clearly safe checks (tests, build, lint). Record the command and a summary of the result. Do not fix problems or change state.

### 3. Build a state table

Label every item as: Done / In progress / Not started / Blocked / Abandoned.

Back each item with evidence: a file path, a command and its output, a commit hash, or the relevant point from the conversation. Label unsupported claims as "inference" or "assumption".

### 4. Find gaps and ask

Ask only about things you cannot discover and that would change how the next agent works: implicit acceptance criteria, business context, external permissions, verbal agreements, priorities, and intended next steps.

- Ask 2–5 numbered questions per round, each with your recommended answer.
- Update the state table after the user answers, then decide whether another round is needed. There is no hard round limit; one extra round is cheaper than leaving a critical assumption blank.
- Label every unverified judgment in the package as an "assumption".

### 5. Write the package

Read [references/handover-template.md](references/handover-template.md) and follow it:

- `HANDOVER.md`: complete state, evidence, decisions, dead ends, artifact map, environment, risks, and next steps.
- `SYSTEM_PROMPT_NEXT.md`: a ready-to-paste opening prompt. Include the goal, hard constraints, state summary, abandoned paths, first action, and definition of done. Tell the new agent to read `HANDOVER.md` first, but keep the prompt usable if that file cannot be read.

Then read the relevant section of [references/domain-checklists.md](references/domain-checklists.md) for the task type and fill in its specific items. Do not load unrelated sections.

Use project-relative paths in `HANDOVER.md`. Use absolute paths in `SYSTEM_PROMPT_NEXT.md` so the next conversation can open them directly.

If `handover/` already exists, create a new timestamped directory, read the latest package, carry forward what is still valid, and add a "Changes since the last handover" section (added / changed / no longer valid).

### 6. Self-check

Before delivering, verify:

- Can a fresh agent answer: what are we building, why, where are we now, which paths are closed, what is the next action, what counts as done, how do I run it, and where is the evidence?
- Every "Done" has evidence; every next step is an executable action; every path exists.
- No API keys, passwords, tokens, or personal data.
- Nothing planned is presented as done; no failure or unverified conclusion is hidden.
- `SYSTEM_PROMPT_NEXT.md` still works when pasted on its own.

End `HANDOVER.md` with 3–6 project-specific acceptance checks that make the new agent restate the critical state before acting.

### 7. Deliver

Report the absolute paths of both files and one sentence on how to use the package next time. Do not modify any other project file.

## Quality bar

- No vague instructions such as "continue the previous work".
- Do not replay long conversations; extract decisions, reasons, and evidence.
- Never delete or overwrite an older handover.
- Never write secret values; record only variable names, config locations, and how to obtain them.
- If context is nearly exhausted, write a minimal usable package first, then improve it incrementally.

## When not to use

If the user only needs a short conversation summary and no project inspection, use a lighter handoff flow (for example, the `handoff` skill when available).
