# 配文与平台改写

## 主配文（抖音/小红书，约 250 字）

换 agent 后，最贵的不是 token，是重新解释项目。

我以前交接项目，是把聊天记录复制给新对话。
结果它还是不知道：目标变过几次、哪些方案已经失败、代码现在到底是什么状态。

后来我改成两份文件：

`HANDOVER.md`：目标、进度、决策、死路、产物、环境、风险，每条尽量带证据。

`SYSTEM_PROMPT_NEXT.md`：新对话的开局提示，直接写清硬约束、当前状态和第一步。

新 agent 先读交接包，再核对文件与 git 状态，然后才动手。
它不会把“计划”当成“已完成”，也不会把已经失败的路再走一遍。

这个 skill 叫 project-handover。
Codex / Claude Code 都能用。

安装：
`npx skills@latest add NormanGOING/project-handover`

如果你也受够了上下文重置后从头解释，试试它。

## 抖音口播版（30–45 秒）

换 agent 后，我终于不用从头解释项目了。

以前交接，就是复制聊天记录。
现在交接，是两份文件。

一份写清目标、决策、死路和证据；
一份直接告诉新 agent：下一步做什么。

它会先核对文件状态，再动手。
不会把计划当成已完成，也不会重复踩坑。

project-handover，Codex 和 Claude Code 都能用。
安装命令在评论区。

## 小红书版

标题：换 agent 后，我终于不用从头解释项目了

正文：

最近把 AI 项目的交接方式改了一下，效果比我预期好。

以前换对话，我的做法是把聊天记录整段复制过去。
但新 agent 还是会问：
「现在做到哪了？」
「之前为什么不用另一个方案？」
「这些改动提交了吗？」

后来我改成两份文件：

1️⃣ `HANDOVER.md`
目标、进度、决策、死路、产物、环境、风险，每条尽量带证据。

2️⃣ `SYSTEM_PROMPT_NEXT.md`
新对话的开局提示，直接写清硬约束、当前状态和第一步。

关键是它不只需要“总结”，还会检查对话、文件、git 状态和测试结果。
信息冲突时也不猜，会把两种说法都写进“待确认”。

项目叫 project-handover，已经开源。
Codex / Claude Code 都能用。

安装：
`npx skills@latest add NormanGOING/project-handover`

#AI编程 #Codex #ClaudeCode #上下文管理 #效率工具 #开源项目 #独立开发

## 知乎/V2EX 版

标题：为什么聊天记录不适合作为项目交接？

多轮对话后，项目最常见的失真不是“忘了细节”，而是三件事混在了一起：

1. 对话里说过的意图；
2. 文件系统里的当前事实；
3. 已经试过但失败的方向。

聊天记录能保留第 1 点，却很难准确表达第 2、3 点。新 agent 看到的是一长串讨论，不知道哪条结论已经被推翻，也不知道当前分支有没有未提交修改。

我把交接拆成两份文件：

- `HANDOVER.md`：状态表、决策记录、死路、产物地图、环境、风险、下一步，尽量为每条结论附路径、命令或提交作为证据。
- `SYSTEM_PROMPT_NEXT.md`：可直接粘贴的接手提示，包含目标、硬约束、状态摘要、第一步和完成标准。

设计上刻意做了两个区分：文件和 git 是“当前状态”的准绳，对话是“目标与取舍”的准绳；两者冲突时不静默裁决，而是写进“不一致项”。

这个 skill 默认只读，不改代码、不移动文件、不提交、不切分支，适合在上下文快耗尽或换 agent 时使用。

仓库：https://github.com/NormanGOING/project-handover
安装：`npx skills@latest add NormanGOING/project-handover`

## X/LinkedIn 英文版

Most “agent handoffs” are just chat summaries.

They lose the reasons, the dead ends, and the actual state of the repo.

`project-handover` inspects the conversation, files, git state, and tests, then writes:

- `HANDOVER.md` — goals, current state, decisions, dead ends, artifacts, and evidence
- `SYSTEM_PROMPT_NEXT.md` — a ready-to-paste resume prompt

Read-only by default. Works with Codex and Claude Code.

`npx skills@latest add NormanGOING/project-handover`

## GitHub Release 文案

**v0.1.0 — Hand over the project, not the chat.**

`project-handover` generates a complete, resumable handover package for a fresh AI agent:

- `HANDOVER.md`: goals, state, decisions, dead ends, artifacts, environment, risks, and next steps.
- `SYSTEM_PROMPT_NEXT.md`: a self-contained prompt the next conversation can start from.

The skill inspects the conversation, project files, git state, and safe runtime checks before writing. It is read-only by default, never writes secret values, and creates timestamped snapshots instead of overwriting older handovers.

Install:

```bash
npx skills@latest add NormanGOING/project-handover
```

## 评论区置顶

安装命令：`npx skills@latest add NormanGOING/project-handover`

仓库：https://github.com/NormanGOING/project-handover

如果你试了，欢迎告诉我：哪一部分最有帮助？哪一部分最难填？
