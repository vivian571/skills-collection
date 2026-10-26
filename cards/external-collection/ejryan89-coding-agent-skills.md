# EJRyan89/coding-agent-skills（可移植编码 agent 技能）

- 分类: 外部收藏
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/EJRyan89/coding-agent-skills
- 调用: 未安装，收藏备查
- 一句话: 横跨 Claude Code / Codex / Copilot CLI 的可移植技能——审配置、审技能、清仓库、审 PR、管记忆，15 个 SKILL.md。

## 说明

2026-10-25 验真：GitHub 搜索 API 实查 ★2，MIT，pushed 2026-10-25；树验真：skills/ 下 15 个 SKILL.md（audit-ai-config、audit-skill、curate-agent-memory、repo-cleanup、review-prs、github-activity-report、dotnet-format 等；另有测试固件里的 SKILL.md 不计入）。技能指令以 Claude 格式为准，Codex 与 Copilot 经生成的适配器读取；附带受 guard 的部署器，把机器相关配置渲染进不可变模板。发现渠道：2026-10-25 GitHub topic:agent-skills 搜索，当日验真通过。功能域：编码 agent 治理 / 代码审查 / 仓库管理。

## 边界

仅收藏登记，未安装未实测。repo-cleanup、curate-agent-memory 等技能会改动仓库与记忆，取用前先读其审批与回滚说明。
