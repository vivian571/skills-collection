# heartleo/zlib（Z-Library 命令行工具）

- 分类: 外部收藏
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/heartleo/zlib
- 调用: 未安装，收藏备查
- 一句话: Z-Library 的命令行工具：在终端里搜书、下载，推送到 Kindle 与微信读书，并通过 MCP 与插件让 AI agent 直接代办找书下书。

## 说明

2026-11-20 验真：GitHub API 与仓库原文实查，★2,516、fork 176，MIT，Go 语言，仓库建于 2026-04-10，pushed 2026-11-19（仍活跃）。主页 https://zlib.heartleo.dev/ 。功能：按年份/语言/格式搜书、浏览收藏与推荐与下载历史、查账号每日下载额度、推送 Kindle、导入微信读书书架、镜像域名连通性自检（doctor）与代理支持。使用前提：自备 Z-Library 账号，先找可用镜像域名再登录，登录态存本地。Agent 集成是它的主打：内置 MCP 服务（`zlib mcp`），并提供 Claude Code / Codex / Grok 插件；插件自带技能，树内有多个 SKILL.md（如 plugins/zlib/skills/zlib/SKILL.md、kindle、metadata 等，另有 .agents/skills/ 下的 zlib、zlib-tui 等）。官方 Agent 设置说明要求用户本人执行 `zlib login`，让密码不进聊天记录。发现渠道：Vivian 2026-11-20 发来仓库链接，点选只收藏登记成卡。

## 边界

仅收藏登记，未安装未运行，未做代码安全审查——真要用之前须先审（重点看它如何存登录态、MCP 服务的权限面、install.sh 做什么）。内容层面的灰色是主要风险：Z-Library 是影子图书馆，库内书籍大多未经版权授权，域名屡被查封、镜像频繁更换（doctor 找镜像正源于此）；与 Vivian 已有的 gutenberg 公版书路线（合法、藏书以英文公版为主）性质相反，此卡只作情报备查，不代表可用其下载受版权保护的书籍。
