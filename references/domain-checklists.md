# Domain Checklists

Read only the section for the current task type. Add applicable items to the handover package. If something is unknown and would affect the handover, add it to the question list.

中文版：[domain-checklists.zh-CN.md](domain-checklists.zh-CN.md)

## Code / architecture

- Repository root, branch, HEAD, uncommitted and untracked files, stashes, remote divergence
- Runtime versions, package manager, lockfile, install command
- Start, build, test, lint, and typecheck commands with their latest results
- Entry points, core modules, data flow, external dependencies, API contracts
- Database / schema / migrations, feature flags, deployment state
- Known errors, log locations, reproduction steps
- Credential locations (variable names or config files only)
- Unfinished refactors, temporary patches, TODOs
- Acceptance method for the next change (automated tests or manual steps)

Ask: unpushed local changes, special environment variables, private dependencies, tools that cannot be installed automatically.

## Research / experiments

- Research question, hypotheses, current conclusion and confidence
- Datasets / versions / splits / preprocessing
- Models and hyperparameters, random seeds, framework versions
- Hardware and compute constraints, runtime per run
- Benchmark results and metrics already produced (raw numbers, definitions)
- Rejected hypotheses and why
- Figure, table, and appendix status
- Citation library, target journal, formatting requirements
- Writing progress and experiments still needed
- Reproducible commands

Ask: results not yet in the conversation, metric definitions, hard constraints from advisors or reviewers.

## Multi-agent / workflows

- Roles and responsibility boundaries
- Message / task schemas, state machine, timeout and retry policy
- Tools and MCP services, permissions, where authentication lives
- Long-running jobs, queues, scheduled tasks, and their current state
- Human approval points
- Known failure modes and fallback strategies
- Where memory or state is stored

Ask: which permissions the new agent inherits, which actions require human approval.

## Long-form writing / scripts / planning

- Core premise, target audience, format, and word count
- Finalized outline and chapter status
- Worldbuilding, character sheets, glossary, timeline
- Style guide and forbidden devices
- Known continuity errors and foreshadowing list
- Draft versions and the authoritative version
- Whether the next step is drafting, revising, or unifying style
- Abandoned plots and settings

Ask: draft or polish next, which settings must not change.

## Operations / deployment

- Environment list and access method (no secrets)
- IaC, configuration, image versions
- Backup and rollback steps
- Monitoring, alerts, log locations
- Current incidents, change freezes
- Ownership and contacts
- Last change and its result

Ask: any change in progress, who can approve a release.

## General

- Deadlines, stakeholders, budget, compliance and privacy requirements
- External dependencies and waiting items
- Things the user explicitly said not to do
