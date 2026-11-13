# Chinese Novelist（中文小说创作助手）

- 分类: 写作与出版
- 来源: 外部
- 许可: MIT License（上游为 PenglongHuang/chinese-novelist-skill）
- 位置: https://github.com/PenglongHuang/chinese-novelist-skill · 安装命令：`npx skills add PenglongHuang/chinese-novelist-skill`
- 调用: 「用 chinese-novelist 帮我写一部 XX 的小说」「继续上次写到第 X 章」「用并行模式写我的《XXX》」
- 一句话: 三层递进式问答 + 偏好记忆 + 三种写作模式 + 自动字数校验，让 Agent 从零生成 10–50 章完整中文长篇小说

## 说明

面向 Coding Agent 的中文长篇小说创作系统，当前稳定版 v2.3.2，GitHub 4,857 star（2026-11-13），MIT 许可。核心设计：

**六阶段流程**：
- Phase 0 — 初始化：加载用户偏好、检测中断项目并续写
- Phase 1 — 三层递进式问答：L1 核心定位（必答）、L2 深度定制（可合并两次问）、L3 标题生成（AI 出候选）
- Phase 2 — 规划确认：产出大纲 + 人物档案 + 写作计划 JSON，等待二次确认
- Phase 2.5 — 写作模式选择：串行 / 子Agent并行 / AgentTeams
- Phase 3 — 疯狂创作：全程无需用户确认，逐章严格按大纲执行
- Phase 4 — 自动校验：字数 / 完成度检查，不合格章节重写 ≤3 轮

**三大黄金法则**：展示而非讲述 · 冲突驱动剧情 · 悬念承上启下

**创作记忆系统**：每次创作后学习你的偏好（题材类型、叙事风格、章节数量倾向、文字密度），下次直接复用。

兼容 agent：Claude Code、Cursor、Codex、OpenCode、Aider。参考文档含 9 份 flows + 10 份 guides。

## 边界

- 需要 coding agent 才能运行，WorkBuddy 仅作为对话层入口；实际执行依赖 upstream 源码（本包只镜像 reference 文档与 SKILL.md 说明）。
- Phase 3「疯狂创作」阶段会完全自主推进，无法中途打断或干预——如果希望保留人工审核权，请选择串行模式并在 Phase 2 充分细化大纲。
- README 含 Infistar.cc affiliate link 推广文案，与本技能无关。
- 上游仓库无 `.gitignore`，clone 前建议先读 repository settings。
- 创作生成的小说版权归 AI 输出者依据适用法律处理；本 repo 不声明对创作产物的主张。
