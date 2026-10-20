# project-handover

[English](README.md) | [简体中文](README.zh-CN.md)

> 在换对话、换 agent、上下文过长或阶段性收尾时，把当前项目完整交给下一个 agent，而不是丢给它一段聊天摘要。

**它是什么：** 一个 Codex / Claude Code skill。它会检查对话、项目文件、git 状态和环境，然后生成 `HANDOVER.md` 与 `SYSTEM_PROMPT_NEXT.md`。交接的是“可执行的状态”，不是聊天记录。

## 输出什么

- `HANDOVER.md`：目标、进度、决策、已废弃路径、产物地图、环境、风险、下一步，每条尽量带证据。
- `SYSTEM_PROMPT_NEXT.md`：可直接粘贴到新对话的开局提示，包含硬约束、状态摘要、第一步和完成标准。

## 为什么需要它

多轮对话后常见的问题：

- 目标在讨论中漂移，新对话不知道真正要交付什么。
- 上下文被旧尝试污染，重复走已经失败的路。
- 口头结论没有落盘，换 agent 后全部丢失。
- 只交接“聊了什么”，没有交接“项目现在是什么状态”。

这个 skill 会先检查对话、项目文件、git 状态、配置和测试结果，再生成交接包。信息对不上时，它不会替你猜，而是把冲突写进 `HANDOVER.md` 的“不一致项”。

## 安装

### Codex

```bash
git clone <repo-url> ~/.codex/skills/project-handover
```

Windows PowerShell：

```powershell
git clone <repo-url> "$env:USERPROFILE\.codex\skills\project-handover"
```

### Claude Code

`SKILL.md` 使用相同格式，可以放到：

```bash
git clone <repo-url> ~/.claude/skills/project-handover
```

也可以复制到项目的 `.claude/skills/` 目录。

### 其他 agent

把 `SKILL.md` 和 `references/` 一起提供给它，或在自定义指令中引用 `SKILL.md`。这个 skill 不依赖 Codex 专有 API；`agents/openai.yaml` 只用于 Codex 的界面展示。

## 使用

直接说：

- “用 project-handover 交接当前项目。”
- “上下文太长了，帮我重置上下文并生成交接包。”
- “做一次阶段性总结，下一个 agent 要接手。”

也可以显式调用 `$project-handover`。

默认输出位置：

```text
<项目根>/handover/<YYYY-MM-DD-HHmm>/
├── HANDOVER.md
└── SYSTEM_PROMPT_NEXT.md
```

每次新建时间戳目录，不覆盖旧交接。

## 它会检查什么

| 来源 | 内容 |
|---|---|
| 对话 | 目标、用户纠正、已否决方案、承诺、未解决问题 |
| 文件 | 目录结构、文档、配置、依赖、测试、脚本、日志 |
| git | 分支、HEAD、未提交与未跟踪文件、stash、远端差距 |
| 环境 | 运行时、安装方式、外部服务、硬件、关键路径 |
| 运行状态 | 测试、build、lint 的命令与最近结果 |

## 安全边界

- 默认只读：不改代码、不移动文件、不提交、不切分支、不 stash、不 reset。
- 不写入密钥、密码、令牌的值，只记录变量名或配置文件位置。
- 不覆盖或删除旧交接。
- 发现项目结构需要调整时，只给迁移清单，逐项确认后才动手。

## 输出示例（节选）

```markdown
## 0. 一页速览

- 一句话目标：交付一个只依赖 Python 标准库的内存版 Todo API。
- 当前状态：新增/列出已实现并有测试；完成操作已写但未提交、未测试。
- 下一步：确认索引约定，为 `complete` 补测试，再实现 HTTP 路由。
- 最大风险：README 称“API”，但仓库里没有 HTTP 服务入口。
```

```markdown
## 4. 死路与否定约束

| 不要再尝试 | 失败原因 | 证据 | 何时可以重试 |
|---|---|---|---|
| SQLite 持久化 | 写入时报 `unable to open database file` | `DECISIONS.md` | 部署环境提供可写目录后 |
| 引入 Flask | 部署机不能安装第三方包 | `README.md` | 部署约束改变后 |
```

完整结构见 [交接模板](references/handover-template.zh-CN.md)（英文原版：[handover-template.md](references/handover-template.md)）。

## 设计原则

1. **先查后问。** 能从文件、git 和日志查到的事实，不问用户。
2. **事实与意图分开。** 文件和 git 决定“当前状态”，对话决定“目标与取舍”；冲突显式记录。
3. **覆盖完整，引用不复制。** 产物给路径和一句话说明，不把旧文档再抄一遍。
4. **死路要写死。** 明确写出“不要再尝试什么”和原因，避免新 agent 重复踩坑。
5. **可执行。** 每个下一步都要有动作、产出和完成标准。

## 任务类型

[任务类型清单](references/domain-checklists.zh-CN.md)（英文原版：[domain-checklists.md](references/domain-checklists.md)）提供额外检查项：

- 代码 / 架构开发
- 论文 / 科研 / 实验
- 多 agent / 工作流
- 长文 / 剧本 / 策划
- 运维 / 部署

只读取当前任务相关的小节。

## 语言

Skill 以英文为主版本，中文为完整翻译：

- [SKILL.zh-CN.md](SKILL.zh-CN.md)
- [交接模板](references/handover-template.zh-CN.md)
- [任务类型清单](references/domain-checklists.zh-CN.md)

## 局限

- 只能交接已经被记录或能从项目中发现的信息。只在人脑里的背景需要你回答。
- 超大仓库建议按模块分几次交接，而不是一次列出所有文件。
- 生成的接手提示词仍建议由你快速过一遍，再交给新 agent。

## 贡献

欢迎提 issue 或 PR。请保持一个原则：**增加的是判断依据，不是更多固定步骤。**

## License

MIT
