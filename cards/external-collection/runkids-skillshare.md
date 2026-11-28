# runkids/skillshare（技能跨工具同步管理器）

- 分类: 外部收藏
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/runkids/skillshare
- 调用: 未安装，收藏备查
- 一句话: 给技能、agent、MCP、插件与 hook 一个统一的家：一处编辑，同步到 Claude Code、Codex、Pi、OpenCode 等多个 AI 工具，附技能安全审计与团队共享。

## 说明

2026-11-28 日采验真：GitHub API 实查 ★3,396，许可 MIT，最近 pushed 2026-11-27，默认分支 main。仓库树共 10 个 SKILL.md：可交付技能 1 个（skills/skillshare/，即 skillshare 自身的技能），其余 9 个位于 .skillshare/skills/ 下，为仓库内部开发技能（changelog、code-review、implement-feature、release、update-docs 等），不作可交付登记。工具本体为 Go 编写的 CLI 与桌面应用：技能、agent、规则、MCP 连接与 hook 一处管理，同步到各工具；内置 audit 在技能进入 agent 前扫描；支持团队共享（项目内 .skillshare/ 随代码分发）与本地检查点提交；另有 Web 仪表盘。发现渠道：网页搜索新发现（Hyperautomation Labs 2026-11-22 本周趋势榜第 8 项）。功能域：技能管理 / 多工具同步 / 安全审计。

## 边界

仅收藏登记，未安装未实测；本仓主体是技能同步 CLI 与桌面应用，技能只是其管理对象与附带内容；官方快捷安装为管道脚本入 shell，Homebrew 为更稳妥的安装方式，只登记不写步骤。
