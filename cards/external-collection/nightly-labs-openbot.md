# nightly-labs/openbot（本地优先的多智能体桌面工作台）

- 分类: 外部收藏
- 来源: 外部
- 许可: PolyForm Noncommercial 1.0.0（非商业许可；商业使用需另向版权方申请，0.1.11 及之前版本为 Apache-2.0）
- 位置: https://github.com/nightly-labs/openbot
- 调用: 未安装，收藏备查
- 一句话: 本地优先的桌面工作台，给每个 AI 队友一个独立工作区和会话，可跑 Codex、Claude、Grok 等多个 agent 并让它们互相协作。

## 说明

2026-10-28 验真：Vivian 微信发来交办收藏；GitHub 页面一手核对，公开仓，2026-08-12 创建，★2,621，fork 264，提交 2,249 次，未归档。树内含 `.agents/skills/` 目录与 `marketplace/` 目录，另有本地技能（Local skills）一节，符合外部收藏的“含技能”口径，但本体是一个 Electron 桌面应用（SolidJS + TypeScript + Bun），不是纯技能包。

功能：每个 agent 独立工作区与会话；支持 Codex、Claude、Grok、OpenCode、Gemini、Cursor CLI、Cline CLI（经 ACP）；消息队列（暂停/恢复/取消、崩溃安全持久化）；agent 间消息、回复、表情与文件传输；内嵌浏览器（agent 可打开、检查、控制）；可选 Computer Use（macOS/Windows/Linux，经 cua-driver）；按 agent 的模型、推理、通知、浏览器与面板状态；支持 macOS 13+（Apple Silicon/Intel）、Windows 10+、Linux AppImage，另有无屏服务器与 Docker 部署方式。

## 边界

仅收藏登记，未安装未实测。开发预览状态，README 明确警告：agent 目前以 `danger-full-access` 与 `approvalPolicy: never` 运行，首次明确同意后不再逐动作确认，可读写文件、跑命令、上网、控制内嵌浏览器——只跑可信的 agent 与任务，用前备份并先读 SECURITY.md。许可为非商业，商用前需另取授权，这点与纯 MIT/Apache 技能不同。
