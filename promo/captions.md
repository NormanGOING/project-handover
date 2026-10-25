# 配文与平台改写

## 主配文（抖音/小红书）

长期项目最贵的，不是写代码，是上下文越积越厚。

聊天记录、临时方案、失败尝试、日志、旧结论，全都堆在上下文里。
每开一个新对话，都要重新喂一遍；几千甚至几万 token 被重复消耗，钱在重复花，额度在重复消耗，模型还要在一堆噪音里找重点。
更麻烦的是上下文污染：旧目标、废弃方案、过时结论混在一起，模型的注意力被稀释，容易把已经否定的路再走一遍。

我后来不再用聊天记录交接，而是生成两份文件：

`HANDOVER.md`：不是只写几条硬约束，而是把项目交接需要的类目尽量补齐——目标与验收、当前进度、关键决策及理由、死路、产物地图、环境与依赖、数据与参数、已知问题、未验证假设、下一步和接手验收。

`SYSTEM_PROMPT_NEXT.md`：给新对话的开局提示，写清目标、约束、当前状态和第一步。

它还会根据项目类型主动反思：代码、科研、写作、多 agent、运维，各自该补什么；发现信息缺口时，会先追问，而不是替你猜。

新 agent 先读交接包，再核对文件与 git 状态，然后才动手。
它不是“更长的摘要”，而是把项目状态、决策和证据重新整理成可执行的交接。

这个 skill 叫 project-handover。
Codex / Claude Code 都能用。
安装：
`npx skills@latest add NormanGOING/project-handover`

最后说重一点：
别再拿几千到几万 token 的聊天记录当交接文档了。
它不会让新 agent 更懂项目，只会让它更贵、更慢，更容易被旧上下文带偏。
先交接状态，再让新 agent 开工。

## 抖音口播版（30–45 秒）

长期项目最贵的，不是写代码，是上下文越积越厚。

聊天记录、失败尝试、旧结论全堆在一起，每次新对话都要重新喂一遍，token 在重复烧，模型还要在噪音里找重点。

我把交接改成两份文件：
一份把目标、决策、死路、证据和下一步补齐；
一份直接告诉新 agent 怎么接手。

项目不同，它还会主动追问没写清楚的地方。

别再拿几万 token 的聊天记录当交接文档了，它只会让新 agent 更贵、更慢、更容易被带偏。

project-handover，Codex 和 Claude Code 都能用。
安装命令在评论区。

## 小红书版

标题：长期项目最贵的，不是写代码，是上下文越积越厚

正文：

做长期项目，我最近才意识到一个很隐蔽的成本：不是代码越写越多，而是上下文越积越厚。

聊天记录、临时方案、失败尝试、日志、旧结论，全都堆在上下文里。
每开一个新对话，都要重新喂一遍；几千甚至几万 token 被重复消耗，钱在重复花，额度在重复消耗。

更麻烦的是上下文污染：
旧目标、废弃方案、过时结论混在一起，模型的注意力被稀释，容易把已经否定的路再走一遍。

我后来改成两份文件交接：

1️⃣ `HANDOVER.md`
不是只写几条硬约束，而是把交接类目尽量补齐：
目标与验收、当前进度、关键决策及理由、死路、产物地图、环境与依赖、数据与参数、已知问题、未验证假设、下一步和接手验收。

2️⃣ `SYSTEM_PROMPT_NEXT.md`
给新对话的开局提示，写清目标、约束、当前状态和第一步。

它还会根据项目类型主动反思：代码、科研、写作、多 agent、运维，各自该补什么；发现信息缺口时，会先追问，而不是替你猜。

新 agent 先读交接包，再核对文件与 git 状态，然后才动手。
它不是“更长的摘要”，而是把项目状态、决策和证据重新整理成可执行的交接。

项目叫 project-handover，已经开源。
Codex / Claude Code 都能用。

安装：
`npx skills@latest add NormanGOING/project-handover`

#AI编程 #Codex #ClaudeCode #上下文管理 #上下文污染 #效率工具 #开源项目 #独立开发

## 知乎/V2EX 版

标题：为什么聊天记录不适合作为长期项目的交接文档？

长期项目最隐蔽的成本，不是代码量，而是上下文体积。

聊天记录、临时方案、失败尝试、日志和旧结论不断堆积。每开一个新对话，这些内容都可能被重新喂一遍：几千甚至几万 token 被重复消耗，成本持续上升，额度持续消耗，响应也会变慢。

更严重的是上下文污染。旧目标、废弃方案和过时结论混在一起，模型的注意力被稀释，容易把已经否定的路再走一遍。聊天记录能保留“说过什么”，却很难准确表达“项目现在是什么状态”。

我把交接拆成两份文件：

- `HANDOVER.md`：不只是硬约束，而是覆盖目标与验收、当前进度、决策及理由、死路、产物地图、环境与依赖、数据与参数、已知问题、未验证假设、下一步和接手验收。每条尽量附路径、命令或提交作为证据。
- `SYSTEM_PROMPT_NEXT.md`：可直接粘贴的接手提示，包含目标、硬约束、状态摘要、第一步和完成标准。

它还会按项目类型读取不同检查项：代码、科研、写作、多 agent、运维；发现查不到但会影响接手的信息时，会主动追问，而不是替用户猜。

设计上刻意区分了两件事：文件和 git 是“当前状态”的准绳，对话是“目标与取舍”的准绳；冲突不静默裁决，而是写进“不一致项”。

这个 skill 默认只读，不改代码、不移动文件、不提交、不切分支，适合在上下文快耗尽或换 agent 时使用。

仓库：https://github.com/NormanGOING/project-handover
安装：`npx skills@latest add NormanGOING/project-handover`

## X/LinkedIn 英文版

Long projects don't just accumulate code. They accumulate context.

Chat logs, abandoned approaches, logs, and stale conclusions pile up. Every new session re-feeds the same history: thousands of tokens consumed again, higher cost, slower responses, and diluted attention.

The real problem is context pollution. Old goals and rejected plans blur the model's focus, so it retries paths that were already ruled out.

`project-handover` replaces the chat log with two files:

- `HANDOVER.md` — not just hard constraints. It covers goals, acceptance criteria, progress, decisions, dead ends, artifacts, environment, dependencies, data, known issues, assumptions, next steps, and handover checks.
- `SYSTEM_PROMPT_NEXT.md` — a ready-to-paste resume prompt.

It also reads domain-specific checklists for code, research, writing, multi-agent workflows, and operations, then asks about gaps instead of guessing.

Read-only by default. Works with Codex and Claude Code.

`npx skills@latest add NormanGOING/project-handover`

Stop using a chat log as a handoff document. It doesn't make the next agent smarter; it makes it more expensive, slower, and easier to mislead.

## GitHub Release 文案

**v0.1.0 — Hand over the project, not the chat.**

Long projects accumulate context: chat history, abandoned approaches, logs, and stale conclusions. Re-feeding that history into every new session consumes tokens, slows responses, and dilutes the model's attention.

`project-handover` generates a complete, resumable handover package for a fresh AI agent:

- `HANDOVER.md`: goals, acceptance criteria, state, decisions, dead ends, artifacts, environment, dependencies, data, known issues, assumptions, next steps, and handover checks.
- `SYSTEM_PROMPT_NEXT.md`: a self-contained prompt the next conversation can start from.

The skill inspects the conversation, project files, git state, and safe runtime checks before writing. It reads domain-specific checklists for code, research, writing, multi-agent workflows, and operations, and asks about gaps instead of guessing. It is read-only by default, never writes secret values, and creates timestamped snapshots instead of overwriting older handovers.

Install:

```bash
npx skills@latest add NormanGOING/project-handover
```

## 评论区置顶

你现在的交接方式是哪一种：

1. 直接复制聊天记录
2. 写一份 README
3. 让新 agent 自己翻代码猜
4. 能让它直接说出目标、死路和下一步

project-handover 是第 4 种。

安装：`npx skills@latest add NormanGOING/project-handover`
仓库：https://github.com/NormanGOING/project-handover
