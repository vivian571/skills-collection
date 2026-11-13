# CATALOG · 技能总索引

共 287 张卡，7 个分类。本文件由 `scripts/build_catalog.py` 自动生成，不要手改。

## 写作与出版

### [supervisor-writing（写作子集）](cards/writing-publishing/supervisor-writing.md)

- 一句话: 把港科大（广州）骆昱宇老师十年顶会经验炼成的 6 个写作技能，适配到文章/书稿写作流程。
- 来源: 改编
- 许可: CC BY-NC-SA 4.0（仅个人非商用）
- 位置: ~/workspace/custom-skills/local-supervisor-writing/
- 调用: 「评估一下这个选题」「帮我预审这篇文章」

### [wechat-draft-publisher（公众号草稿箱发布）](cards/writing-publishing/wechat-draft-publisher.md)

- 一句话: Markdown → 公众号样式 HTML → 经官方 API 进草稿箱，到此为止，发表永远手动。
- 来源: 自建
- 许可: 自有（源仓库 vivian571/wechat-publisher）
- 位置: ~/workspace/custom-skills/local-wechat-draft-publisher/
- 调用: 「把这篇推到公众号草稿箱」

## 分析与诊断

### [agent-trace（Agent 轨迹分析三件套）](cards/analysis-diagnosis/agent-trace.md)

- 一句话: 把 Agent 的 JSONL 轨迹投影成执行链，并重建每次请求的上下文做 token 尸检。
- 来源: 改编
- 许可: 思路源自 xuanyuanzhifeng/dsh-plugin-agent-workflow（MIT），代码独立重写
- 位置: ~/workspace/custom-skills/local-agent-trace/
- 调用: 「看一下这次 agent 跑了什么」「这次调用为什么这么贵」

### [six-layer-analysis（六层分析法）](cards/analysis-diagnosis/six-layer-analysis.md)

- 一句话: 把一个问题从信息、逻辑、系统、人性、意义到行动/验证逐层看透。
- 来源: 自建
- 许可: 自有
- 位置: ~/workspace/custom-skills/local-six-layer-analysis/
- 调用: 「全面分析」「用六层分析」「帮我拆一下这件事」「值不值得投入」

## 逆向工程

### [rea-reverse（REA 逆向工作流轻量版）](cards/reverse-engineering/rea-reverse.md)

- 一句话: 反编译 → 追踪 → 带证据和局限的结论 → 复现，三条逆向线各一个技能。
- 来源: 改编
- 许可: 蒸馏自 morluto/rea 的工作流，后端工具均为开源
- 位置: ~/workspace/custom-skills/local-rea-reverse/
- 调用: 「扒一下这个 APK 的登录逻辑」

## 视频与视觉

### [anatomy（等距技术图解）](cards/video-visual/anatomy.md)

- 一句话: 把一个技术概念画成精细的交互式等距 SVG 实物图（仪表、机柜、锁具式的物理对象）。
- 来源: 外部
- 许可: MIT
- 位置: ~/workspace/custom-skills/local-anatomy/
- 调用: 「用 anatomy 画一张 XX 原理图」

### [kaomei/stickman-video-director（火柴人视频导演）](cards/video-visual/kaomei-stickman-video-director.md)

- 一句话: 把主题、文章或脚本变成火柴人视频：导演模式出分镜脚本和逐场生成提示词，Autopilot 模式本地渲染带配音、字幕、微动效的成片。
- 来源: 外部（已安装本地）
- 许可: MIT
- 位置: ~/workspace/custom-skills/local-stickman-video-director/（技能名 directing-stickman-videos；上游 https://github.com/kaomei/stickman-video-director）
- 调用: 「用火柴人导演模式做一段 XX」「用 Autopilot 模式把这篇稿子成片」

### [sweety-handdraw-video（手绘讲解视频）](cards/video-visual/sweety-handdraw-video.md)

- 一句话: 根据主题或讲解稿制作带封面的完整手绘讲解视频，按实际配音逐字安排描线与填色。
- 来源: 改编
- 许可: MIT（上游 LICENSE）
- 位置: ~/workspace/custom-skills/local-sweety-handdraw-video/
- 调用: 「做一个手绘讲解视频」（每日 08:00 手绘 cron 亦走此管线）

### [video-kb（短视频知识库）](cards/video-visual/video-kb.md)

- 一句话: 把短视频转写并提炼成可搜索的知识库笔记，接进个人档案馆。
- 来源: 自建
- 许可: 自有
- 位置: ~/workspace/custom-skills/local-video-kb/
- 调用: 「把这个视频收进知识库」「抖音视频提炼」「把这条群分享视频入库」

## 行为与决策

### [human-cheat-codes（人类作弊器）](cards/behavior-decision/human-cheat-codes.md)

- 一句话: 五本行为科学经典拆出的 31 个实战战术，呼叫时出战斗卡。
- 来源: 自建
- 许可: 自有（战术提炼自五本公开出版物）
- 位置: ~/workspace/custom-skills/local-human-cheat-codes/
- 调用: 点名战术代号，或描述场景（谈判议价、沉没成本、重大决策、拖延启动、说服、被甩锅）

## 教育与学习

### [edulab（教育技能集合）](cards/education-learning/edulab.md)

- 一句话: 把学科问题转成可交互的教学网页和带配音的讲解视频，6 个子技能。
- 来源: 外部
- 许可: Apache-2.0
- 位置: ~/workspace/custom-skills/local-edulab/（上游 https://github.com/wy51ai/edulab）
- 调用: 「解这道立体几何题」「随机出一道圆锥曲线题」「把这道物理题做成讲解视频」

## 外部收藏

### [1npo/dossier（带引用、可定位提交的 HTML 调研档案）](cards/external-collection/1npo-dossier.md)

- 一句话: Claude Code 调研档案技能：产出带引用、按提交定位来源的 HTML 档案，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/1npo/dossier
- 调用: 未安装，收藏备查

### [AIPMAndy/ClearSkill（磁盘清理决策技能）](cards/external-collection/aipmandy-clearskill.md)

- 一句话: 帮 Claude Code 做安全的磁盘清理决策——先判断能不能删、再决定怎么删的单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/AIPMAndy/ClearSkill
- 调用: 未安装，收藏备查

### [Agents365-ai/drawio-skill（自然语言转 Draw.io 图技能）](cards/external-collection/agents365-ai-drawio-skill.md)

- 一句话: 把自然语言、代码、Terraform/K8s 配置、SQL、OpenAPI、AsyncAPI、Protobuf 等转成 Draw.io 图表的单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Agents365-ai/drawio-skill
- 调用: 未安装，收藏备查

### [AgriciDaniel/claude-ads（付费媒体运营技能）](cards/external-collection/agricidaniel-claude-ads.md)

- 一句话: Claude-first 的付费媒体运营技能：覆盖 12 个广告平台的投放、审计、预算、创意与归因，共 34 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/AgriciDaniel/claude-ads
- 调用: 未安装，收藏备查

### [AgriciDaniel/claude-obsidian（Obsidian 第二大脑技能）](cards/external-collection/agricidaniel-claude-obsidian.md)

- 一句话: 给 Claude Code 的自组织 Obsidian 第二大脑：wiki 检索、摄入、整理、研究、画布等 15 个可交付技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/AgriciDaniel/claude-obsidian
- 调用: 未安装，收藏备查

### [AgriciDaniel/claude-seo（通用 SEO 技能库）](cards/external-collection/agricidaniel-claude-seo.md)

- 一句话: Claude Code 通用 SEO 技能：技术 SEO、E-E-A-T、结构化数据、GEO/AEO、agent 可读性、外链、本地 SEO 等，树内 35 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/AgriciDaniel/claude-seo
- 调用: 未安装，收藏备查

### [Alisa0808/vox-director（Vox 拼贴讲解视频技能）](cards/external-collection/alisa0808-vox-director.md)

- 一句话: 把一个主题自动做成 Vox 风纸拼贴讲解/广告视频的 agent skill，全流程跑在 Atlas Cloud + ffmpeg 上。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Alisa0808/vox-director
- 调用: 未安装，收藏备查

### [ApolloMonasa/contest-solver（编程竞赛做题工作流）](cards/external-collection/apollomonasa-contest-solver.md)

- 一句话: 编程竞赛做题工作流 agent 技能：调研→补问→规划→TDD→分批提交→提测循环，按 Agent Skills 标准格式写成。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/ApolloMonasa/contest-solver
- 调用: 未安装，收藏备查

### [AwayerCode/Harn（技能作项目依赖）](cards/external-collection/awayercode-harn.md)

- 一句话: 把技能当成项目依赖来管：版本化、可审计、可复现，换机器换人也能装出同一套技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/AwayerCode/Harn
- 调用: 未安装，收藏备查

### [BofAI/skills（Bank of AI 技能集，含 x402-payment）](cards/external-collection/bofai-skills.md)

- 一句话: Bank of AI 的技能合集仓（TRON 生态为主）；其中的 x402-payment 技能让 agent 用 USDT/USDD/USDC 经 x402 协议为付费 API 付款（带 --dry-run 与单笔上限）。
- 来源: 外部（其中 x402-payment 已安装本地）
- 许可: MIT
- 位置: https://github.com/BofAI/skills（x402-payment 本地安装：~/workspace/custom-skills/local-x402-payment/）
- 调用: 未启用付款通道，收藏备查

### [CTO-DRS/design-arsenal（设计武器库）](cards/external-collection/cto-drs-design-arsenal.md)

- 一句话: 设计武器库单技能：根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/CTO-DRS/design-arsenal
- 调用: 未安装，收藏备查

### [CathyErer/frog-and-toad-studio（按章节生成教学材料）](cards/external-collection/cathyerer-frog-and-toad-studio.md)

- 一句话: 给 Claude 与 Codex 的教学材料生成技能：按章节产出配套教学内容，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/CathyErer/frog-and-toad-studio
- 调用: 未安装，收藏备查

### [ChaseSunstrom/sampo（通用 agent 插件技能集）](cards/external-collection/chasesunstrom-sampo.md)

- 一句话: 通用 agent 插件技能集：头脑风暴、捕获、调试测试、设计提取、诊断等，共 24 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/ChaseSunstrom/sampo
- 调用: 未安装，收藏备查

### [Codewithaiyan/reforge-mcp（代码库分析 MCP 技能）](cards/external-collection/codewithaiyan-reforge-mcp.md)

- 一句话: 把代码库分析做成 Claude Code 的 MCP 工具：扫描、风险打分、打补丁，并明说哪些读不到，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Codewithaiyan/reforge-mcp
- 调用: 未安装，收藏备查

### [ComposioHQ/awesome-claude-skills（巨型技能汇编）](cards/external-collection/composiohq-awesome-claude-skills.md)

- 一句话: 号称清单、实际把 864 个 SKILL.md 本体汇编进仓的巨型合集，默认分支是 master。
- 来源: 外部
- 许可: 见上游（API 未标注 SPDX；内含各技能许可不一）
- 位置: https://github.com/ComposioHQ/awesome-claude-skills
- 调用: 未安装，收藏备查

### [Cotal-AI/Cotal（Agent 协同开放标准）](cards/external-collection/cotal-ai-cotal.md)

- 一句话: 面向 agent 协同的开放标准与技能包，7 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/Cotal-AI/Cotal
- 调用: 未安装，收藏备查

### [DietrichGebert/ponytail（懒人程序员思维技能）](cards/external-collection/dietrichgebert-ponytail.md)

- 一句话: 让 AI agent「像最懒的老程序员一样思考」——review/audit/debt/gain 四件套加主技能，共 13 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/DietrichGebert/ponytail
- 调用: 未安装，收藏备查

### [Donchitos/Claude-Code-Game-Studios（游戏开发工作室技能集）](cards/external-collection/donchitos-claude-code-game-studios.md)

- 一句话: 把 Claude Code 变成一间完整的游戏开发工作室：自称 49 个 AI agent、72 个工作流技能，按真实工作室层级协调，从点子到上线。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Donchitos/Claude-Code-Game-Studios
- 调用: 未安装，收藏备查

### [DozenTwelve/Papermorph（书转动画互动网页技能）](cards/external-collection/dozentwelve-papermorph.md)

- 一句话: 把一本书变成带动画、旁白、可交互的网页体验的 AI 技能，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/DozenTwelve/Papermorph
- 调用: 未安装，收藏备查

### [EJRyan89/coding-agent-skills（可移植编码 agent 技能）](cards/external-collection/ejryan89-coding-agent-skills.md)

- 一句话: 横跨 Claude Code / Codex / Copilot CLI 的可移植技能——审配置、审技能、清仓库、审 PR、管记忆，15 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/EJRyan89/coding-agent-skills
- 调用: 未安装，收藏备查

### [EbrahimAbdelwahed/cold-email-skill（个性化 cold email 技能）](cards/external-collection/ebrahimabdelwahed-cold-email-skill.md)

- 一句话: 写让人真正回复的 cold email：定目标、挖背景、起草、过质检、经你点头才发，再安排跟进。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/EbrahimAbdelwahed/cold-email-skill
- 调用: 未安装，收藏备查

### [Egonex-AI/Understand-Anything（代码知识图谱理解技能）](cards/external-collection/egonex-ai-understand-anything.md)

- 一句话: 把任何代码变成可探索、可搜索的交互式知识图谱——「Graphs that teach > graphs that impress」，9 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Egonex-AI/Understand-Anything
- 调用: 未安装，收藏备查

### [Ekko237/award-polish（网站与界面打磨技能）](cards/external-collection/ekko237-award-polish.md)

- 一句话: 给 agent 的网站、Web 应用与 App 界面打磨技能：按获奖级标准逐项抛光，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Ekko237/award-polish
- 调用: 未安装，收藏备查

### [Ekko237/copy-studio（分阶段营销文案流水线）](cards/external-collection/ekko237-copy-studio.md)

- 一句话: 给 Claude Code / Codex 的分阶段营销文案流水线技能：按阶段走完定位、起草、打磨，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Ekko237/copy-studio
- 调用: 未安装，收藏备查

### [Ekko237/imagegen-swarm（并行调用各家出图额度）](cards/external-collection/ekko237-imagegen-swarm.md)

- 一句话: 把你已经付费的各家 AI 出图额度一次性并行用起来：一个提示多家同时出图，再挑最好的，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Ekko237/imagegen-swarm
- 调用: 未安装，收藏备查

### [EminBudak/launch-film（产品启动视频技能）](cards/external-collection/eminbudak-launch-film.md)

- 一句话: 从网站或 App Store 页面做一条启动视频：用产品真实的 logo、配色、字体与界面截图，本地渲染，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/EminBudak/launch-film
- 调用: 未安装，收藏备查

### [GangJaeYu/harness_loop_full_korean（韩语 agent 开发循环）](cards/external-collection/gangjaeyu-harness-loop-full-korean.md)

- 一句话: 韩语 Claude Code / Codex agent 技能插件：想法→PRD→设计→任务→验证 harness→自主开发循环，13 个技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/GangJaeYu/harness_loop_full_korean
- 调用: 未安装，收藏备查

### [Gentleman-Programming/gentle-shell（Pi 原生并行开发工作台技能）](cards/external-collection/gentleman-programming-gentle-shell.md)

- 一句话: Pi 原生的 AI 辅助开发工作台技能：并行编码 agent、实时任务、Git diff 回顾，15 个技能覆盖分支、PR、评审与文档。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Gentleman-Programming/gentle-shell
- 调用: 未安装，收藏备查

### [HelloYeew/dotnet-skill（个人 C#/.NET 偏好技能）](cards/external-collection/helloyeew-dotnet-skill.md)

- 一句话: 作者个人的 C# 代码风格与 .NET 偏好技能：常用库与 Sakura Framework 用法指南，单技能。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/HelloYeew/dotnet-skill
- 调用: 未安装，收藏备查

### [HeyChengC/vibe-knowledge-film（抖音风 Vibe 知识短片技能）](cards/external-collection/heychengc-vibe-knowledge-film.md)

- 一句话: 抖音爆款 Vibe 知识大赏知识短片 skill：拆爆款视频、复刻画风、排导演分镜表、自动配音效，一键出片，根目录 1 个 SKILL.md。
- 来源: 外部（本地已安装同源技能）
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/HeyChengC/vibe-knowledge-film（本地安装：~/workspace/custom-skills/local-vibe-knowledge/）
- 调用: 未安装，收藏备查

### [HsuanYuLee/polaris（Claude Code 工作区模板技能）](cards/external-collection/hsuanyulee-polaris.md)

- 一句话: 带 AI 技能的 Claude Code 工作区模板：JIRA、PR、代码评审、估算等 16 个技能，覆盖从需求到交付的工程流程。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/HsuanYuLee/polaris
- 调用: 未安装，收藏备查

### [Illyism/seo-skills（开源 SEO 技能集）](cards/external-collection/illyism-seo-skills.md)

- 一句话: 给 Claude Code、Cursor、Codex 等 AI agent 的开源 SEO 技能：作者自营站点的 12 套 SKILL.md 工作流，树内 30 个 SKILL.md（含多 harness 复本）。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/Illyism/seo-skills
- 调用: 未安装，收藏备查

### [Jakeschincariol/day-trader-skill（日内交易 11 技能）](cards/external-collection/jakeschincariol-day-trader-skill.md)

- 一句话: 11 个日内交易技能：扫描大量图表、盯突发新闻、掐进出场时机、事前复盘每一次结果再动真钱。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Jakeschincariol/day-trader-skill
- 调用: 未安装，收藏备查

### [Jakeschincariol/founder-skill（创业者开局验证 11 技能）](cards/external-collection/jakeschincariol-founder-skill.md)

- 一句话: 上线前先验证生意的 11 个免费 Claude 技能：受 Hormozi、Thiel、Jobs 启发的董事会、品牌、CFO、竞品、定价与发布。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Jakeschincariol/founder-skill
- 调用: 未安装，收藏备查

### [Jakeschincariol/instagram-agent-skill（13 个 Instagram 运营技能）](cards/external-collection/jakeschincariol-instagram-agent-skill.md)

- 一句话: 13 个跑 Instagram 账号的 Claude 技能：按 26 条打分钩子公式写 Reels、病毒研究、标题校对、轮播图、评论转私信与人味改写，共 13 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Jakeschincariol/instagram-agent-skill
- 调用: 未安装，收藏备查

### [Jakeschincariol/replica-skill（复刻任意应用的 11 个技能）](cards/external-collection/jakeschincariol-replica-skill.md)

- 一句话: 11 个复刻任意应用的 Claude 技能：侦察、设计、后端、架构、构建、部署、上线、差异比对、品牌与创业复盘，走完从看到到上线。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Jakeschincariol/replica-skill
- 调用: 未安装，收藏备查

### [JasonHMY/personal-finance-visualizer（本地交互式财务报告）](cards/external-collection/jasonhmy-personal-finance-visualizer.md)

- 一句话: 让 agent 把财务数据做成本地交互式报告：圆形图、交易钻取，中英双语，记忆优先处理。
- 来源: 外部
- 许可: MIT-0
- 位置: https://github.com/JasonHMY/personal-finance-visualizer
- 调用: 未安装，收藏备查

### [Jeffallan/claude-skills（全栈开发者 67 技能）](cards/external-collection/jeffallan-claude-skills.md)

- 一句话: 67 个面向全栈开发者的专项技能：架构、API、云、数据库、调试、DevOps、Django/FastAPI 等各一岗。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Jeffallan/claude-skills
- 调用: 未安装，收藏备查

### [JetBrains/thinkrail（轻量 IDE 氛围编程）](cards/external-collection/jetbrains-thinkrail.md)

- 一句话: JetBrains 出品的轻量真实 IDE，用 pi 做氛围编程，IDE 会围绕使用者工作方式自我定制，12 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/JetBrains/thinkrail
- 调用: 未安装，收藏备查

### [JimLiu/baoyu-design（本地 Claude Design 技能）](cards/external-collection/jimliu-baoyu-design.md)

- 一句话: 在本地跑 Claude Design 的 agent 技能：高保真 mockup、交互原型、deck、线框图，做成自包含 HTML，不用上 claude.ai/design。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/JimLiu/baoyu-design
- 调用: 未安装，收藏备查

### [JimLiu/baoyu-skills（中文自媒体技能集）](cards/external-collection/jimliu-baoyu-skills.md)

- 一句话: 22 个中文向自媒体技能：封面图、信息图、漫画、公众号/微博/X/小红书发布、视频转写等。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/JimLiu/baoyu-skills
- 调用: 未安装，收藏备查

### [JuliusBrussee/caveman（洞穴人省 token 技能）](cards/external-collection/juliusbrussee-caveman.md)

- 一句话: viral 技能：「why use many token when few token do trick」——用洞穴人说话风给 coding agent 省 65% token，28 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/JuliusBrussee/caveman
- 调用: 未安装，收藏备查

### [JuneYaooo/rea-video（视频逐镜逆向技能）](cards/external-collection/juneyaooo-rea-video.md)

- 一句话: 逆向一切视频，逐镜拆出制作方式并给出复刻方案：判断每镜是实拍、AI 生成还是代码生成，再拆字幕、剪辑与声音怎么做，单技能。
- 来源: 外部（本地已安装同源技能）
- 许可: Apache-2.0
- 位置: https://github.com/JuneYaooo/rea-video（本地安装：~/workspace/custom-skills/local-rea-video/）
- 调用: 未安装，收藏备查

### [K-Dense-AI/scientific-agent-skills（科学技能库）](cards/external-collection/k-dense-scientific-agent-skills.md)

- 一句话: 把 AI agent 变成科研助手的技能库，177 个 SKILL.md，是本批单库体量最大的一个。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/K-Dense-AI/scientific-agent-skills
- 调用: 未安装，收藏备查

### [KKKKhazix/agent-autoloop（命令行 Agent 后台接活跟进）](cards/external-collection/kkkkhazix-agent-autoloop.md)

- 一句话: 让命令行 Agent 在后台自己接活、自己跟进到底：平时不烦你，遇到拿不准的事才发卡片找你拍板，核心技能 1 个，另附 10 个示例配方。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/KKKKhazix/agent-autoloop
- 调用: 未安装，收藏备查

### [KKKKhazix/khazix-skills（数字生命卡兹克的 AI 技能合集）](cards/external-collection/kkkkhazix-khazix-skills.md)

- 一句话: 中文向 AI 技能合集 6 个：定目标的 leader、洁癖 neat-freak、热点分析、写作、存储分析。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/KKKKhazix/khazix-skills
- 调用: 未安装，收藏备查

### [Kulaxyz/self-learning-skills（会话最优路径沉淀）](cards/external-collection/kulaxyz-self-learning-skills.md)

- 一句话: 自我改进技能：把会话里来之不易的「黄金路径」自动沉淀为可复用 skill，支持 Claude Code/Cursor/AGENTS.md 等 70+ agent。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Kulaxyz/self-learning-skills
- 调用: 未安装，收藏备查

### [Leonxlnx/taste-skill（给 agent 审美的技能）](cards/external-collection/leonxlnx-taste-skill.md)

- 一句话: 给 coding agent 装上审美：美术指导、参考图与浏览器实机检查，替代千篇一律的 AI 网页，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Leonxlnx/taste-skill
- 调用: 未安装，收藏备查

### [Lusona/ai-skills（迭代式产品工程技能）](cards/external-collection/lusona-ai-skills.md)

- 一句话: 迭代式产品与工程技能：结果、证据、授权、TDD 与有界批量协作都写明，共 14 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Lusona/ai-skills
- 调用: 未安装，收藏备查

### [MSKazemi/reachweaver（社媒排期技能）](cards/external-collection/mskazemi-reachweaver.md)

- 一句话: Claude Code 社媒技能：证据驱动排期、审批优先发布、发布工作流与复盘分析，2 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/MSKazemi/reachweaver
- 调用: 未安装，收藏备查

### [Motionsites-AI/claude-skill（电影感落地页技能）](cards/external-collection/motionsites-ai-claude-skill.md)

- 一句话: 免费 Claude 技能，让 Claude 做出获奖级、电影感的落地页，单技能。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/Motionsites-AI/claude-skill
- 调用: 未安装，收藏备查

### [NAJEMWEHBE/studio-skills（从纠错里攒经验的自我改进技能）](cards/external-collection/najemwehbe-studio-skills.md)

- 一句话: 给 Claude 的经验教训日志：从纠错里起草教训、经你批准、反复出现的就沉淀成规则，附直播示例，共 2 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/NAJEMWEHBE/studio-skills
- 调用: 未安装，收藏备查

### [NVIDIA/SkillSpector（技能安全扫描器）](cards/external-collection/nvidia-skillspector.md)

- 一句话: NVIDIA 出品的 AI agent 技能安全扫描器：查技能里的漏洞、恶意模式与过度授权，可交付技能 1 个。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/NVIDIA/SkillSpector
- 调用: 未安装，收藏备查

### [Nanako0129/sepia（去 AI 味写作技能）](cards/external-collection/nanako0129-sepia.md)

- 一句话: 给任何兼容 Agent Skills 的 agent 用的去 AI 味写作技能：写作、审校、重构三件套，共 6 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Nanako0129/sepia
- 调用: 未安装，收藏备查

### [NevaMind-AI/memU（跨 Agent 个人记忆）](cards/external-collection/nevamind-ai-memu.md)

- 一句话: 跨 agent 的个人记忆技能，让不同 agent 共享同一份个人记忆，1 个 SKILL.md。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/NevaMind-AI/memU
- 调用: 未安装，收藏备查

### [NiazMorshed2007/reanimate（动画逐帧逆向技能）](cards/external-collection/niazmorshed2007-reanimate.md)

- 一句话: 把任意动画逐帧逆向拆解，再证明复刻版的动作与原版一致，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/NiazMorshed2007/reanimate
- 调用: 未安装，收藏备查

### [Nutlope/hallmark（反 AI 味设计技能）](cards/external-collection/nutlope-hallmark.md)

- 一句话: 让 agent 做的网页不再一眼 AI 味的反 slop 设计技能：先立硬底线，再放手做设计。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Nutlope/hallmark
- 调用: 未安装，收藏备查

### [OWENWANG-GULIAI/guliai-skills（谷粒 AI 实用技能合集）](cards/external-collection/owenwang-guliai-guliai-skills.md)

- 一句话: 谷粒 AI 的实用型 agent 技能合集：内容生产、个人品牌、课程设计、社群运营与 skill 开发，含微信自动化方向技能。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/OWENWANG-GULIAI/guliai-skills
- 调用: 未安装，收藏备查

### [Orchestra-Research/AI-Research-SKILLs（AI 研究与工程技能库）](cards/external-collection/orchestra-research-ai-research-skills.md)

- 一句话: 面向 AI 研究与工程的开源技能库：模型架构、分词、微调、机理可解释、数据处理、后训练等方向共 98 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Orchestra-Research/AI-Research-SKILLs
- 调用: 未安装，收藏备查

### [OthmanAdi/planning-with-files（文件型持久规划）](cards/external-collection/othmanadi-planning-with-files.md)

- 一句话: 用文件做持久规划的单技能 —— 同一份 SKILL.md 适配 12+ harness（Claude/Cursor/Codex/Gemini 等），另带 5 语言 i18n 版。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/OthmanAdi/planning-with-files
- 调用: 未安装，收藏备查

### [OyadotAI/oya-browser（浏览器控制平面技能）](cards/external-collection/oyadotai-oya-browser.md)

- 一句话: 给 AI agent 的浏览器控制平面技能：统一 API 接 Oya Cloud、Browserbase、Steel 等，带持久身份与验证码处理，22 个 SKILL.md。
- 来源: 外部
- 许可: 见上游（API 标注 NOASSERTION）
- 位置: https://github.com/OyadotAI/oya-browser
- 调用: 未安装，收藏备查

### [PaodingAI/skills（文档解析技能）](cards/external-collection/paodingai-skills.md)

- 一句话: 把 PDF、DOCX、PPT 等文档解析成 Markdown 的可复用技能，另含招股书审计、对话文档等文档工作流技能。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/PaodingAI/skills
- 调用: 未安装，收藏备查

### [Platanor/hardware-compliance-handbook（欧盟硬件合规知识库技能）](cards/external-collection/platanor-hardware-compliance-handbook.md)

- 一句话: 把欧盟硬件合规法规（CRA、RED 网络安全规则、NIS2、EUCC 认证框架）做成 agent 可读的知识库技能，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/Platanor/hardware-compliance-handbook
- 调用: 未安装，收藏备查

### [Ryze-AI-Adgent/open-seo-mcp-skills（SEO 与 GEO 技能集）](cards/external-collection/ryze-ai-adgent-open-seo-mcp-skills.md)

- 一句话: 免费的 SEO MCP 服务器 + 开源 SEO/GEO 技能：关键词研究、竞品缺口、外链检查、排名追踪、SEO 审计等 8 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills
- 调用: 未安装，收藏备查

### [SHARPLEE00/lookbk-skills（视频/幻灯片/图片/网页技能）](cards/external-collection/sharplee00-lookbk-skills.md)

- 一句话: 给 Claude Code、Codex、Cursor 的免费技能：做视频、幻灯片、图片和网页，7 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/SHARPLEE00/lookbk-skills
- 调用: 未安装，收藏备查

### [SandroDuarsa/lawful-ui（让 UI 遵守法律的技能）](cards/external-collection/sandroduarsa-lawful-ui.md)

- 一句话: 让 agent 建出的 Web 与 App 界面遵守法律：合规检查做进构建流程，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/SandroDuarsa/lawful-ui
- 调用: 未安装，收藏备查

### [ScrapeGraphAI/just-scrape（网页抓取转结构化数据技能）](cards/external-collection/scrapegraphai-just-scrape.md)

- 一句话: 一句话把任意网址变成 Markdown、结构化 JSON、截图或链接清单的抓取技能，还带多页爬取与页面变化定时监测。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/ScrapeGraphAI/just-scrape
- 调用: 未安装，收藏备查

### [Servosity/msp-skills（MSP 工具技能集）](cards/external-collection/servosity-msp-skills.md)

- 一句话: 面向 MSP（托管服务商）的免费 MCP 服务器 + Claude Code 技能：PSA、RMM、备份、M365 等工具，共 104 个 SKILL.md。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/Servosity/msp-skills
- 调用: 未安装，收藏备查

### [SnailSploit/Claude-Red（进攻性安全技能库）](cards/external-collection/snailsploit-claude-red.md)

- 一句话: 面向 Claude 技能系统的进攻性安全技能库：按攻击面分 23 类的方法论 SKILL.md，共 79 个。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/SnailSploit/Claude-Red
- 调用: 未安装，收藏备查

### [Stophyuk/solutionzip-skills（问题解决集日常技能 10 个）](cards/external-collection/stophyuk-solutionzip-skills.md)

- 一句话: 作者日常工作用的 10 个 Claude Code 技能：卡片新闻、短视频、App 体检、AI 味检查、文案校对、单机服务器等。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Stophyuk/solutionzip-skills
- 调用: 未安装，收藏备查

### [SupercmoHQ/superCMO-skills（AI 营销官技能包）](cards/external-collection/supercmohq-supercmo-skills.md)

- 一句话: 把 Claude/Cursor/Codex 变成 AI CMO —— 端到端营销 campaign 技能包：UGC 视频、广告视频、产品摄影等，共 23 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/SupercmoHQ/superCMO-skills
- 调用: 未安装，收藏备查

### [Vincentwei1021/video-shotcraft（AI 视频制作技能）](cards/external-collection/vincentwei1021-video-shotcraft.md)

- 一句话: 给 Claude Code 与 Codex 的 AI 视频技能：做电影感、可编辑的产品宣传片，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/Vincentwei1021/video-shotcraft
- 调用: 未安装，收藏备查

### [VoltAgent/awesome-agent-skills（1000+ 技能清单）](cards/external-collection/voltagent-awesome-agent-skills.md)

- 一句话: 清单型合集：自称收录 1000+ 来自官方团队与社区的 agent skill（兼容 Claude Code / Codex / Gemini CLI / Cursor 等），仓内只有清单没有 SKILL.md 本体。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/VoltAgent/awesome-agent-skills
- 调用: 未安装，收藏备查

### [VoltAgent/awesome-openclaw-skills（OpenClaw 技能清单）](cards/external-collection/voltagent-awesome-openclaw-skills.md)

- 一句话: 清单型合集：自称收录 5,400+ 经筛选分类的 OpenClaw 技能，仓内只有清单没有 SKILL.md 本体。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/VoltAgent/awesome-openclaw-skills
- 调用: 未安装，收藏备查

### [Weaverse/.agents（AI 编码 agents、技能与规则集）](cards/external-collection/weaverse-agents.md)

- 一句话: AI 编码用的 agents、技能、命令与规则合集：调试日志、修 PR、发版验证、数据库迁移评审等，共 12 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Weaverse/.agents
- 调用: 未安装，收藏备查

### [WenyuChiou/ai-research-skills（科研工作流技能目录·清单）](cards/external-collection/wenyuchiou-ai-research-skills.md)

- 一句话: 科研工作流技能目录：文献综述、研究设计、项目记忆、稿件写作、跨 agent 分派 —— 以 catalog/skills.yml 形式收录的清单型合集（仓内无 SKILL.md 本体）。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/WenyuChiou/ai-research-skills
- 调用: 未安装，收藏备查

### [WenyuChiou/awesome-agentic-ai-zh（中文 Agentic AI 学习路线图）](cards/external-collection/wenyuchiou-awesome-agentic-ai-zh.md)

- 一句话: 繁中 / English / 简中三语 Agentic AI 学习路线图：从 LLM 基础到多智能体系统，240+ 精选资源与动手示例，附 1 个示例 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/WenyuChiou/awesome-agentic-ai-zh
- 调用: 未安装，收藏备查

### [aaron-he-zhu/aaron-marketing-skills（120 个营销技能）](cards/external-collection/aaron-he-zhu-aaron-marketing-skills.md)

- 一句话: 一支可安装的 AI 营销团队——叙事、SEO/GEO、社媒、邮件、付费广告、网红、发布 7 大学科共 120 个技能。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/aaron-he-zhu/aaron-marketing-skills
- 调用: 未安装，收藏备查

### [abdelaalimouid/qgis-agent（QGIS 与遥感技能）](cards/external-collection/abdelaalimouid-qgis-agent.md)

- 一句话: 给 Claude Code 的 QGIS 与遥感技能：先规划、再写带编号的 PyQGIS 脚本、核验结果、出事实工作报告，覆盖 Sentinel-2、NDVI、分类、面积与制图，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/abdelaalimouid/qgis-agent
- 调用: 未安装，收藏备查

### [addyosmani/agent-skills（工程技能库）](cards/external-collection/addyosmani-agent-skills.md)

- 一句话: Addy Osmani 出品的生产级工程技能库，25 个 SKILL.md，覆盖 API 设计、代码审查、CI/CD 等。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/addyosmani/agent-skills
- 调用: 未安装，收藏备查

### [affaan-m/ECC（Agent Harness 性能优化系统）](cards/external-collection/affaan-m-ecc.md)

- 一句话: Agent harness 性能优化系统：技能、直觉、记忆、安全与研究优先开发，覆盖 Claude Code、Codex、OpenCode、Cursor 等，树内 1,068 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/affaan-m/ECC
- 调用: 未安装，收藏备查

### [agentkitco/agentkit-dev-skills（日常开发 13 技能）](cards/external-collection/agentkitco-agentkit-dev-skills.md)

- 一句话: 13 个日常开发技能：审 diff、复现优先排障、安全改重构、写 PR 描述、会话交接、审 AGENTS.md 等，全部 MIT。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/agentkitco/agentkit-dev-skills
- 调用: 未安装，收藏备查

### [ahmedmostafa147/whiteboard-lesson（教科书页转阿拉伯语白板讲解视频）](cards/external-collection/ahmedmostafa147-whiteboard-lesson.md)

- 一句话: 把任意教科书页面变成带旁白的阿拉伯语白板动画讲解视频，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/ahmedmostafa147/whiteboard-lesson
- 调用: 未安装，收藏备查

### [aiskillstore/marketplace（技能市场）](cards/external-collection/aiskillstore-marketplace.md)

- 一句话: 技能市场仓库，树内含 6,183 个 SKILL.md，规模异常大，疑为批量收录。
- 来源: 外部
- 许可: 未标注
- 位置: https://github.com/aiskillstore/marketplace
- 调用: 未安装，收藏备查

### [akiiwa-games/AgentCompass（多 agent 任务路由器）](cards/external-collection/akiiwa-games-agentcompass.md)

- 一句话: 确定性多 agent 任务路由器与订阅额度调度器：面向 Claude Code、Codex、Gemini CLI、Grok、Paseo，按模型特性与能力下限分流子 agent，4 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/akiiwa-games/AgentCompass
- 调用: 未安装，收藏备查

### [akshay-diwadkar/first-four-hours（动手前先磨刀的四个小时）](cards/external-collection/akshay-diwadkar-first-four-hours.md)

- 一句话: 编码 agent 别只会挥斧头，先磨刀：学习、意义建构、工作台三组技能，先把问题想清楚再动手，共 15 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/akshay-diwadkar/first-four-hours
- 调用: 未安装，收藏备查

### [alchaincyf/darwin-skill（达尔文 Skill 进化系统）](cards/external-collection/alchaincyf-darwin-skill.md)

- 一句话: 让你的 Skill 无限进化的系统：评估 → 改进 → 测试 → 保留或回滚，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/alchaincyf/darwin-skill
- 调用: 未安装，收藏备查

### [alchaincyf/huashu-art-motion（花叔艺术动画）](cards/external-collection/alchaincyf-huashu-art-motion.md)

- 一句话: 代码绘制的艺术动画技能：35+ 种艺术风格 + 9 种解说语法，流程为镜头表（锁画风/色板/角色）→ storyboard_lint → 逐镜渲染 → 拼接混口播 → qa → deliver 门禁出片。
- 来源: 外部（已安装本地）
- 许可: MIT
- 位置: https://github.com/alchaincyf/huashu-art-motion（本地安装：~/workspace/custom-skills/local-huashu-art-motion/）
- 调用: 「用 huashu 做一条 XX 艺术动画」

### [alchaincyf/huashu-design（花叔设计技能）](cards/external-collection/alchaincyf-huashu-design.md)

- 一句话: 一句话拿回能交付的设计：网页/App 原型、可编辑 PPTX、动画、信息图，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/alchaincyf/huashu-design
- 调用: 未安装，收藏备查

### [alchaincyf/huashu-motion（花叔产品宣传片技能）](cards/external-collection/alchaincyf-huashu-motion.md)

- 一句话: 让 agent 一键直出商业级产品宣传片：会作曲、能指着画面改，导演规则来自实测拆片，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/alchaincyf/huashu-motion
- 调用: 未安装，收藏备查

### [alchaincyf/nuwa-skill（蒸馏任何人思维方式的技能）](cards/external-collection/alchaincyf-nuwa-skill.md)

- 一句话: 蒸馏任何人的思维方式：心智模型、决策启发式、表达 DNA，做成可调用的 agent 技能，附 15 个名人视角示例，共 16 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/alchaincyf/nuwa-skill
- 调用: 未安装，收藏备查

### [alchaincyf/zhangxuefeng-skill（张雪峰认知操作系统）](cards/external-collection/alchaincyf-zhangxuefeng-skill.md)

- 一句话: 张雪峰的认知操作系统：高考志愿、考研、职业规划的实战思维框架，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/alchaincyf/zhangxuefeng-skill
- 调用: 未安装，收藏备查

### [alexsandsouza/spection（AI 引导的软件工程框架技能）](cards/external-collection/alexsandsouza-spection.md)

- 一句话: 开源的 AI 引导软件工程框架：需求、产品简报、架构设计、质量门禁、安全评审、发版，共 9 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/alexsandsouza/spection
- 调用: 未安装，收藏备查

### [alibaba/open-code-review（阿里代码评审技能）](cards/external-collection/alibaba-open-code-review.md)

- 一句话: 阿里规模验证过的混合架构代码评审工具技能：确定性流水线 + LLM agent，行级精准评论，2 个技能。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/alibaba/open-code-review
- 调用: 未安装，收藏备查

### [alirezarezvani/claude-skills（380 技能大合集）](cards/external-collection/alirezarezvani-claude-skills.md)

- 一句话: "380 Claude Code skills & agent skills & plugins" —— 实测树里 465 个 SKILL.md 的综合大合集。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/alirezarezvani/claude-skills
- 调用: 未安装，收藏备查

### [allxsmith/bestax-skills（bestax 编码 agent 插件技能）](cards/external-collection/allxsmith-bestax-skills.md)

- 一句话: bestax 编码 agent 的插件技能：自定义组件、表单、图标、布局脚手架、迁移、优化、主题，共 7 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/allxsmith/bestax-skills
- 调用: 未安装，收藏备查

### [amierlorenz/skills（日常学习与建造技能）](cards/external-collection/amierlorenz-skills.md)

- 一句话: 作者每天自用的 Claude Code 技能——每篇都是能一分钟读完的纯 Markdown，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/amierlorenz/skills
- 调用: 未安装，收藏备查

### [anbeime/skill（中文技能商店精选合集）](cards/external-collection/anbeime-skill.md)

- 一句话: 中文技能商店：精选原创技能包（文档处理、内容创作、编程开发、机器学习、自动化工作流）打包好可直接安装，并自动抓取上游更新。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/anbeime/skill
- 调用: 未安装，收藏备查

### [anjotadena/asterweave（理解仓库、协调专家的 agent 技能集）](cards/external-collection/anjotadena-asterweave.md)

- 一句话: 理解你的仓库、协调多个专家 agent 的技能集：规划、分析、实现、评审、提交 PR、复盘等，共 26 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/anjotadena/asterweave
- 调用: 未安装，收藏备查

### [anthropics/skills（Anthropic 官方技能库）](cards/external-collection/anthropics-skills.md)

- 一句话: Anthropic 官方的 Agent Skills 仓库，skills/ 目录下是一批官方出品的 SKILL.md，可当写法范本。
- 来源: 外部
- 许可: 见仓库内各技能自带 LICENSE（API 未标注统一 SPDX）
- 位置: https://github.com/anthropics/skills
- 调用: 未安装，收藏备查

### [apexstoa/strategy-tester（交易想法回测 verdict）](cards/external-collection/apexstoa-strategy-tester.md)

- 一句话: 拿你自己的交易想法和自己的行情数据做回测，最后给一个数字 verdict：GO、NO-GO 或 INCONCLUSIVE——只给方法，不给信号。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/apexstoa/strategy-tester
- 调用: 未安装，收藏备查

### [appariciojunior/video-editor-skills（DaVinci 粗剪技能）](cards/external-collection/appariciojunior-video-editor-skills.md)

- 一句话: 教 Claude Code 当 DaVinci Resolve 初剪师：转录粗剪、vlog 节奏、B-roll、音乐音效、干净字幕、动效、YouTube 导出，共 12 个 SKILL.md。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/appariciojunior/video-editor-skills
- 调用: 未安装，收藏备查

### [assb-lab/github-issue-flow（Issue 优先的 AI 编码技能）](cards/external-collection/assb-lab-github-issue-flow.md)

- 一句话: Issue 优先的 AI 编码 agent 技能：以 GitHub Issue 为粒度走完需求到实现，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/assb-lab/github-issue-flow
- 调用: 未安装，收藏备查

### [avivsinai/agent-message-queue（本地 agent 间文件消息队列）](cards/external-collection/avivsinai-agent-message-queue.md)

- 一句话: 给本地 agent 用的文件型消息队列（Maildir 风格），让不同 agent 之间能互相传消息、排队协作。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/avivsinai/agent-message-queue
- 调用: 未安装，收藏备查

### [ayghri/i-have-adhd（ADHD 友好输出技能）](cards/external-collection/ayghri-i-have-adhd.md)

- 一句话: 让 coding agent 别再把答案埋在一堆废话里——专为 ADHD 用户设计的输出风格技能，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/ayghri/i-have-adhd
- 调用: 未安装，收藏备查

### [b0bsl3d/InformedVoter（选票转无党派研究指南）](cards/external-collection/b0bsl3d-informedvoter.md)

- 一句话: 把你的样本选票变成无党派研究指南（网页 + PDF）与一页填空选票小抄，附各州投票规则。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/b0bsl3d/InformedVoter
- 调用: 未安装，收藏备查

### [baodhg/FLOW（FLOW Harness 工作流技能包）](cards/external-collection/baodhg-flow.md)

- 一句话: FLOW Harness：带编码 agent 从探索、规划、执行到复盘走完一整套工作流的技能包与 CLI，各仓库上下文留在本地，共 14 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/baodhg/FLOW
- 调用: 未安装，收藏备查

### [benjitaylor/skills（AI 编码 agent 技能）](cards/external-collection/benjitaylor-skills.md)

- 一句话: AI 编码 agent 技能仓，树内 1 个 SKILL.md（stageshow）。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/benjitaylor/skills
- 调用: 未安装，收藏备查

### [bitwize-music-studio/claude-ai-music-skills（人机协作音乐制作技能）](cards/external-collection/bitwize-music-studio-claude-ai-music-skills.md)

- 一句话: 人 + AI 做音乐的全流程技能：给 Suno 用的作词、作曲、混音、母带、专辑概念与宣发，共 53 个 SKILL.md。
- 来源: 外部
- 许可: CC0-1.0
- 位置: https://github.com/bitwize-music-studio/claude-ai-music-skills
- 调用: 未安装，收藏备查

### [blader/humanizer（去 AI 味改写技能）](cards/external-collection/blader-humanizer.md)

- 一句话: 去掉文本里的 AI 生成痕迹、改写成自然人味的 agent 技能，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/blader/humanizer
- 调用: 未安装，收藏备查

### [bmalthi/hal-light（轻量严谨数据分析 agent）](cards/external-collection/bmalthi-hal-light.md)

- 一句话: 轻量 agent 做自动化严谨数据分析：从一句话提示端到端跑完，产出可验证结论的漂亮简报与完整审计轨迹，共 3 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/bmalthi/hal-light
- 调用: 未安装，收藏备查

### [bompus/house-rules（AI 编码 agent 工作规则技能）](cards/external-collection/bompus-house-rules.md)

- 一句话: 给 AI 编码 agent 的工作规则与技能：核心规则、可选修饰层、自定义层与各仓库 AGENTS.md，共 38 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/bompus/house-rules
- 调用: 未安装，收藏备查

### [career-ops-hq/career-ops（AI 求职 agent 技能）](cards/external-collection/career-ops-hq-career-ops.md)

- 一句话: 开源 AI 求职 agent：扫招聘版、按 CV 逐个 1–5 分打分再决定投不投——同一技能适配 7 个 harness，7 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/career-ops-hq/career-ops
- 调用: 未安装，收藏备查

### [caru-ini/stack-diagram（技术栈架构图技能）](cards/external-collection/caru-ini-stack-diagram.md)

- 一句话: 一句话描述你的技术栈，拿回一张带官方 logo 的架构图，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/caru-ini/stack-diagram
- 调用: 未安装，收藏备查

### [cathrynlavery/diagram-design（编辑级图表设计技能）](cards/external-collection/cathrynlavery-diagram-design.md)

- 一句话: 编辑级图表设计技能：45 种图表类型、自包含 HTML + SVG，拒绝阴影与 Mermaid 糊图，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/cathrynlavery/diagram-design
- 调用: 未安装，收藏备查

### [chenf888/TMT-game-generator（增量游戏生成技能）](cards/external-collection/chenf888-tmt-game-generator.md)

- 一句话: 一句话对话生成完整可玩的 The Modding Tree（TMT v2.7）增量放置游戏——采访、设计、脚手架、生成、静态检查、模拟调节奏，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/chenf888/TMT-game-generator
- 调用: 未安装，收藏备查

### [chgagne/claude-skills-research（学术研究支持技能）](cards/external-collection/chgagne-claude-skills-research.md)

- 一句话: 给 Claude Code 的学术研究支持技能：文献调研、书目核验、论文互比、审稿、证明核验与 HPC 实验，共 12 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/chgagne/claude-skills-research
- 调用: 未安装，收藏备查

### [chu0119/pojun-skill（ARTEX 渗透测试方法论技能）](cards/external-collection/chu0119-pojun-skill.md)

- 一句话: ARTEX 方法论蒸馏成的可移植 Agent Skill：三视角协议 + 三账本证据纪律 + 四层安全护栏，任意 AI Agent 即装即用，单技能。
- 来源: 外部
- 许可: AGPL-3.0
- 位置: https://github.com/chu0119/pojun-skill
- 调用: 未安装，收藏备查

### [cloudflare/security-audit-skill（安全审计技能）](cards/external-collection/cloudflare-security-audit-skill.md)

- 一句话: Cloudflare 官方出品：带 coding agent 走六阶段安全审计，产出可独立验证、机器可读的审计结论，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/cloudflare/security-audit-skill
- 调用: 未安装，收藏备查

### [code-yeongyu/oh-my-openagent（图工程技能包）](cards/external-collection/code-yeongyu-oh-my-openagent.md)

- 一句话: 关键词触发的图工程技能包：prompt 里加关键词即可成为图工程主人，含 60 个 SKILL.md。
- 来源: 外部
- 许可: 见上游（GitHub API 未标注 SPDX）
- 位置: https://github.com/code-yeongyu/oh-my-openagent
- 调用: 未安装，收藏备查

### [coreyhaines31/marketingskills（营销技能库）](cards/external-collection/coreyhaines31-marketingskills.md)

- 一句话: 面向 Claude Code 与 AI agent 的营销技能库，52 个 SKILL.md，覆盖 CRO、文案、SEO、广告与数据分析。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/coreyhaines31/marketingskills
- 调用: 未安装，收藏备查

### [crt106/c3rb3r-btrfs-recovery（群晖勒索无密钥恢复）](cards/external-collection/crt106-c3rb3r-btrfs-recovery.md)

- 一句话: 从残存的 Btrfs 写时复制区段里无密钥恢复被 C3RB3R 勒索加密的群晖文件，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/crt106/c3rb3r-btrfs-recovery
- 调用: 未安装，收藏备查

### [cth9191/animate（单画布讲解/故事视频技能）](cards/external-collection/cth9191-animate.md)

- 一句话: 用程序化动画做讲解与故事短视频：单文件画布视频，带故事、画风与分镜确认，7 种内置风格或按你的参考图匹配画风，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/cth9191/animate
- 调用: 未安装，收藏备查

### [curie-eng/curie（Agent 变同事的自托管平台技能）](cards/external-collection/curie-eng-curie.md)

- 一句话: 开源自托管平台 Curie 的附带技能：把 agent 变成同事，从 Software Factory 派发 GitHub issue 起步。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/curie-eng/curie
- 调用: 未安装，收藏备查

### [daveebbelaar/bama（原生 macOS 应用构建技能）](cards/external-collection/daveebbelaar-bama.md)

- 一句话: BAMA：用 agent 技能调研、克隆、设计、构建、优化与测试原生 macOS 应用（Swift + SwiftUI），21 个技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/daveebbelaar/bama
- 调用: 未安装，收藏备查

### [davila7/claude-code-templates（Claude Code 组件注册表与 CLI）](cards/external-collection/davila7-claude-code-templates.md)

- 一句话: Claude Code 组件的开源注册表与 CLI：agents、commands、skills、hooks、MCPs、settings 与 mods，树内 926 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/davila7/claude-code-templates
- 调用: 未安装，收藏备查

### [dcbruck/claude-skills（独立顾问的日常 12 技能）](cards/external-collection/dcbruck-claude-skills.md)

- 一句话: 独立 AI 创意顾问每天自用的 12 个 slash-command 技能：prompt 放大、想法挖掘与分诊、语音锁定起草、转录挖矿、合同审查、系统图等。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/dcbruck/claude-skills
- 调用: 未安装，收藏备查

### [dcc-mcp/dcc-asset-blender-extensions（Blender 扩展商店技能）](cards/external-collection/dcc-mcp-dcc-asset-blender-extensions.md)

- 一句话: DCC-MCP 网关里的 Blender 扩展商店技能——让 agent 经共享网关调用已安装的扩展包技能，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/dcc-mcp/dcc-asset-blender-extensions
- 调用: 未安装，收藏备查

### [dcc-mcp/dcc-asset-godot-store（Godot 资产商店技能）](cards/external-collection/dcc-mcp-dcc-asset-godot-store.md)

- 一句话: DCC-MCP 网关里的 Godot 资产商店技能——让 agent 经共享网关调用已安装的资产包技能，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/dcc-mcp/dcc-asset-godot-store
- 调用: 未安装，收藏备查

### [deanpeters/Product-Manager-Skills（产品经理技能框架）](cards/external-collection/deanpeters-product-manager-skills.md)

- 一句话: 产品经理技能框架：竞品分析、发现访谈、机会树、定价、生命周期、下线流程等实战方法，共 77 个 SKILL.md。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/deanpeters/Product-Manager-Skills
- 调用: 未安装，收藏备查

### [deeprdai21-ai/practical-claude-skills（实用小技能两件套）](cards/external-collection/deeprdai21-ai-practical-claude-skills.md)

- 一句话: 两个免费实用的小技能：给股票导出文件重排列表，以及对一段说法逐条做事实核查。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/deeprdai21-ai/practical-claude-skills
- 调用: 未安装，收藏备查

### [dereknex/immune-brain（Agent 免疫大脑）](cards/external-collection/dereknex-immune-brain.md)

- 一句话: 给 agent 的免疫式工作流技能：澄清、起草、驱动、修 PR、精简文档与测试、复盘，共 9 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/dereknex/immune-brain
- 调用: 未安装，收藏备查

### [dmoreq/agent-grimoire（跨 harness 可移植 AGENTS.md 内核与技能包）](cards/external-collection/dmoreq-agent-grimoire.md)

- 一句话: 可移植的 AGENTS.md 内核与技能包：同一套技能跑在 Grok、Codex、Zed、OpenCode、Antigravity、ZCode 上，共 43 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/dmoreq/agent-grimoire
- 调用: 未安装，收藏备查

### [dreammis/social-auto-upload（社媒自动上传技能）](cards/external-collection/dreammis-social-auto-upload.md)

- 一句话: 自动化上传视频到社交媒体的技能集：抖音、小红书、视频号、TikTok、YouTube、B站等，共 18 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/dreammis/social-auto-upload
- 调用: 未安装，收藏备查

### [e1dred/agent-skills（桌面应用驱动技能）](cards/external-collection/e1dred-agent-skills.md)

- 一句话: 让 agent 动手操作桌面应用的技能：CAD、演示文稿、办公套件、图片处理，共 7 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/e1dred/agent-skills
- 调用: 未安装，收藏备查

### [egguy886/h3-drama-kit（MiniMax H3 AI 短剧全流程技能）](cards/external-collection/egguy886-h3-drama-kit.md)

- 一句话: 端到端 AI 短剧流水线技能：剧本→素材→分镜提示词→质检→AutoDL 生成→审片→后期，从 60 集实战生产里提炼的方法，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/egguy886/h3-drama-kit
- 调用: 未安装，收藏备查

### [elayadesign/ai-design-skills（落地页设计技能）](cards/external-collection/elayadesign-ai-design-skills.md)

- 一句话: 产品设计师的落地页设计技能：先问 offer、买家与唯一行动，再按一套严格的视觉系统出营销页。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/elayadesign/ai-design-skills
- 调用: 未安装，收藏备查

### [elrazez/deepen（任务改写成专业提示词）](cards/external-collection/elrazez-deepen.md)

- 一句话: 动手前先把任务改写成顶级专业人士会写的那种提示词：/deepen 一个指令，覆盖 Claude、Codex、Cursor、Gemini CLI 等约 80 个 agent，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/elrazez/deepen
- 调用: 未安装，收藏备查

### [elvarofficial/teardown（任意机器转 3D 可拆解模拟器技能）](cards/external-collection/elvarofficial-teardown.md)

- 一句话: 一个 Claude Code 技能，把任意机器变成可以拆开的 3D 模拟器，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/elvarofficial/teardown
- 调用: 未安装，收藏备查

### [emilkowalski/skills（设计师与工程师的动画技能）](cards/external-collection/emilkowalski-skills.md)

- 一句话: Emil Kowalski 的设计与动画技能：动效词汇、编排、手势、动画性能与评审，共 19 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/emilkowalski/skills
- 调用: 未安装，收藏备查

### [eternityspring/shuohao-skills（AI 短剧制作技能集）](cards/external-collection/eternityspring-shuohao-skills.md)

- 一句话: AI 短剧制作的 7 个技能：小说改编大纲、角色设定、角色参考图、场景道具设定、剧本、分镜场位、分镜，一路做到可投产的分镜包。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/eternityspring/shuohao-skills
- 调用: 未安装，收藏备查

### [eugenelim/agent-ready-repo（AI 软件团队操作系统）](cards/external-collection/eugenelim-agent-ready-repo.md)

- 一句话: 从想法到上线的完整 AI 软件团队操作系统：发现→构建→发布三条同行监督循环，配精选技能、子 agent 与配置包，树内 215 个 SKILL.md（含多 harness 复本）。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/eugenelim/agent-ready-repo
- 调用: 未安装，收藏备查

### [f-o-x11/deed-page-skill（deed.page 发布技能）](cards/external-collection/f-o-x11-deed-page-skill.md)

- 一句话: 一个 curl 把文件或文件夹发布成永久网址的 agent 技能，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/f-o-x11/deed-page-skill
- 调用: 未安装，收藏备查

### [feimacode/open-design-agent-kit（专业级 UI 设计技能包）](cards/external-collection/feimacode-open-design-agent-kit.md)

- 一句话: 把专业级 UI 设计装进你已在用的编码 agent：自称 270+ 设计技能、150+ 品牌设计系统、160+ 可混搭示例，适配 Copilot Chat、Claude Code、Codex、Cursor。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/feimacode/open-design-agent-kit
- 调用: 未安装，收藏备查

### [finolabs/finolabs-vibecode（AI 编码 agent 工程实践技能）](cards/external-collection/finolabs-finolabs-vibecode.md)

- 一句话: 一套 AI 编码 agent 的工程实践：路由、委派、评审门禁与核验，覆盖 Claude Code、Codex 与 Antigravity，共 20 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/finolabs/finolabs-vibecode
- 调用: 未安装，收藏备查

### [firecrawl/cli（Firecrawl 网页工具技能集）](cards/external-collection/firecrawl-cli.md)

- 一句话: Firecrawl 官方 CLI 与 agent 技能：搜索、抓取、解析、爬取、建站图、交互、监测与研究索引，13 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/firecrawl/cli
- 调用: 未安装，收藏备查

### [firecrawl/firecrawl-workflows（Firecrawl 工作流技能集）](cards/external-collection/firecrawl-firecrawl-workflows.md)

- 一句话: Firecrawl 官方工作流技能集：SEO 审计、竞品情报、线索挖掘、深度研究、知识库等，共 19 个 SKILL.md。
- 来源: 外部
- 许可: ISC
- 位置: https://github.com/firecrawl/firecrawl-workflows
- 调用: 未安装，收藏备查

### [fliqrlabs/instagram-creator-skills（Instagram 创作者技能包）](cards/external-collection/fliqrlabs-instagram-creator-skills.md)

- 一句话: 30 个 Instagram 创作者技能：爆款钩子、Reel 脚本、文案、轮播图与评论转私信玩法，33 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/fliqrlabs/instagram-creator-skills
- 调用: 未安装，收藏备查

### [flyboy-byte/toolbox（PCB/F-Droid/PR 等技能工具箱）](cards/external-collection/flyboy-byte-toolbox.md)

- 一句话: Claude Code 技能工具箱：PCB 设计、F-Droid、上游 PR、项目规划、README、磁盘清理，另带 Linux 修补与小工具。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/flyboy-byte/toolbox
- 调用: 未安装，收藏备查

### [fortunto2/solo-factory（独立开发者创业流水线）](cards/external-collection/fortunto2-solo-factory.md)

- 一句话: 一人公司的整条流水线——调研、验证、脚手架、搭建、规划、构建、部署、上线、复盘，51 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/fortunto2/solo-factory
- 调用: 未安装，收藏备查

### [gaia-harness/gaia（严肃型 Claude Code Harness）](cards/external-collection/gaia-harness-gaia.md)

- 一句话: 严肃型 Claude Code harness：先写规格、每次提交过门禁、每次合并过代码审计团队，共 23 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/gaia-harness/gaia
- 调用: 未安装，收藏备查

### [genfeedai/skills（内容创作与广告技能集）](cards/external-collection/genfeedai-skills.md)

- 一句话: 面向内容创作、SEO、广告、图片提示词与策略的 AI 技能集，含广告、品牌等主题 bundles。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/genfeedai/skills
- 调用: 未安装，收藏备查

### [gengwg/skills（npx 可装技能集）](cards/external-collection/gengwg-skills.md)

- 一句话: 一组偏运维排障的 agent 技能，可用 npx skills add 安装，35 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/gengwg/skills
- 调用: 未安装，收藏备查

### [getcargohq/cargo-skills（GTM 工程技能集）](cards/external-collection/getcargohq-cargo-skills.md)

- 一句话: 给 AI 编码 agent 的 GTM（市场进入）工程技能：建潜客名单、跑外联、搭增长流程，共 20 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/getcargohq/cargo-skills
- 调用: 未安装，收藏备查

### [giostriquer/on-n-off（Claude Code 开关管理桌面应用附带技能）](cards/external-collection/giostriquer-on-n-off.md)

- 一句话: 管理 Claude Code 开关的 Windows/macOS 桌面应用，仓内附带 1 个发布版本技能（release-version）。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/giostriquer/on-n-off
- 调用: 未安装，收藏备查

### [github/awesome-copilot（Copilot 社区合集）](cards/external-collection/github-awesome-copilot.md)

- 一句话: GitHub 官方社区合集：帮你用好 GitHub Copilot 的指令、agent、技能与配置，树内含 465 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/github/awesome-copilot
- 调用: 未安装，收藏备查

### [google/elephant-goldfish-model（Google 规格驱动开发方法 + 技能集）](cards/external-collection/google-elephant-goldfish-model.md)

- 一句话: Google 的规格驱动开发方法：先写规格、评审对齐，再让 agent 按规格实现，附 14 个配套技能。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/google/elephant-goldfish-model
- 调用: 未安装，收藏备查

### [guaikei/dy-diagnosis（抖音账号诊断技能）](cards/external-collection/guaikei-dy-diagnosis.md)

- 一句话: 抖音账号诊断技能：博主作品、作品表现、评论反馈与对标账号，只读公开数据，另支持用户与达人搜索、公域获客与竞品分析，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/guaikei/dy-diagnosis
- 调用: 未安装，收藏备查

### [guaikei/ks-diagnosis（快手账号诊断技能）](cards/external-collection/guaikei-ks-diagnosis.md)

- 一句话: 快手账号诊断技能：博主作品、作品表现、评论反馈与对标账号，只读公开数据，为账号诊断提供结构化 JSON，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/guaikei/ks-diagnosis
- 调用: 未安装，收藏备查

### [guaikei/tt-diagnosis（TikTok 账号诊断技能）](cards/external-collection/guaikei-tt-diagnosis.md)

- 一句话: TikTok 账号诊断技能：博主作品、作品表现、评论反馈与对标账号，只读公开数据，输出多语言结构化 JSON，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/guaikei/tt-diagnosis
- 调用: 未安装，收藏备查

### [guaikei/xhs-diagnosis（小红书账号诊断技能）](cards/external-collection/guaikei-xhs-diagnosis.md)

- 一句话: 小红书账号诊断技能：博主作品、作品表现、评论反馈与对标账号，只读公开数据，为账号诊断提供结构化 JSON，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/guaikei/xhs-diagnosis
- 调用: 未安装，收藏备查

### [hany202507/finance-ai-skills（韩国会计·税务技能）](cards/external-collection/hany202507-finance-ai-skills.md)

- 一句话: 韩国会计师·税务师用的 Claude Code 技能：法人税、附加税、转让所得税、源泉税申报核查，现金流量表、租赁、决算与外部审计，共 17 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/hany202507/finance-ai-skills
- 调用: 未安装，收藏备查

### [heliocosta-dev/revenue-centric-design（收益导向设计技能）](cards/external-collection/heliocosta-dev-revenue-centric-design.md)

- 一句话: 101 条收益导向设计原则：产品设计、转化与行为科学，写成单个可调用的 Claude Code 技能。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/heliocosta-dev/revenue-centric-design
- 调用: 未安装，收藏备查

### [hesreallyhim/awesome-claude-code（Claude Code 资源清单）](cards/external-collection/hesreallyhim-awesome-claude-code.md)

- 一句话: 清单型合集：人工精选的 Claude Code 资源总汇——技能、配置、工具与教程的索引。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/hesreallyhim/awesome-claude-code
- 调用: 未安装，收藏备查

### [heydamir/unslop（去 AI 味界面技能）](cards/external-collection/heydamir-unslop.md)

- 一句话: 把 vibecoding 出来的、一眼 AI 味的界面改成真正设计过的界面，单技能。
- 来源: 外部
- 许可: CC-BY-4.0
- 位置: https://github.com/heydamir/unslop
- 调用: 未安装，收藏备查

### [hfadhlullah/kaizen（先审计划再动手的 agent 流程）](cards/external-collection/hfadhlullah-kaizen.md)

- 一句话: AI agent 先给你看计划再动手、第二个 agent 再检查做完的结果，另含 UI/UX、书、deck 与视频等媒体技能，7 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/hfadhlullah/kaizen
- 调用: 未安装，收藏备查

### [hieuday88/claude-image（Antigravity CLI 出图技能）](cards/external-collection/hieuday88-claude-image.md)

- 一句话: Claude Code 出图技能：经 Antigravity CLI（agy）调用 Google 的 Gemini 图像模型出图，不用付费 API key。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/hieuday88/claude-image
- 调用: 未安装，收藏备查

### [inkatze/planwright（规格驱动开发自动驾驶）](cards/external-collection/inkatze-planwright.md)

- 一句话: 规格驱动开发的自动驾驶：你签字通过规格，带护栏的 agent 舰队负责构建、评审并交付 PR 草稿，你保留签字与合并权。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/inkatze/planwright
- 调用: 未安装，收藏备查

### [irinabuht12-oss/marketing-skills（49 个营销技能）](cards/external-collection/irinabuht12-oss-marketing-skills.md)

- 一句话: 49 个免费营销技能：Google Ads、Meta Ads 审计、SEO、AI 可见度、归因与预算，附 Ryze 广告 MCP 接入说明。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/irinabuht12-oss/marketing-skills
- 调用: 未安装，收藏备查

### [jaemyeong-hwnag/claude-marketplaces（Claude Code 插件市场与工程规范）](cards/external-collection/jaemyeong-hwnag-claude-marketplaces.md)

- 一句话: Claude Code 插件市场：用 hooks、技能与 MCP 强制执行命名规范、GitHub 工作流、AI 测试覆盖、密钥扫描、压力测试与证据式 AI 评审，共 46 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/jaemyeong-hwnag/claude-marketplaces
- 调用: 未安装，收藏备查

### [jamditis/claude-skills-journalism（新闻与学术技能）](cards/external-collection/jamditis-claude-skills-journalism.md)

- 一句话: 面向新闻、媒体与学术的 Claude Code 技能：事实核查、FOIA 信息公开申请、数据处理，另带一套开发工具技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/jamditis/claude-skills-journalism
- 调用: 未安装，收藏备查

### [jangtrinh/design-os-3d-blender（Blender 5.2 agent 操作系统）](cards/external-collection/jangtrinh-design-os-3d-blender.md)

- 一句话: 给 Blender 5.2 的 agent 操作系统：bpy 知识库、AGENT_OK 执行契约、3D 打印生产门禁，让 agent 能动手建模并走到可打印。
- 来源: 外部
- 许可: 见上游（API 标注 NOASSERTION）
- 位置: https://github.com/jangtrinh/design-os-3d-blender
- 调用: 未安装，收藏备查

### [jek-bao-choo/productivity-plugins（效率插件集）](cards/external-collection/jek-bao-choo-productivity-plugins.md)

- 一句话: 四个效率插件的技能集：邮件/Slack 沟通、POC 流程、产品演示、视频剪辑，共 19 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/jek-bao-choo/productivity-plugins
- 调用: 未安装，收藏备查

### [jnMetaCode/superpowers-zh（superpowers 中文增强版）](cards/external-collection/jnmetacode-superpowers-zh.md)

- 一句话: obra/superpowers 的完整汉化 + 4 个中国原创技能：中文代码评审、中文提交规范、中文文档、中文 Git 工作流，共 21 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/jnMetaCode/superpowers-zh
- 调用: 未安装，收藏备查

### [john-walks-slow/rabbit-skills（轻量 Coding Agent 配置套件）](cards/external-collection/john-walks-slow-rabbit-skills.md)

- 一句话: 轻量、松弛、有效的 Coding Agent 配置套件，面向中等规模 AI 原生项目开发，19 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/john-walks-slow/rabbit-skills
- 调用: 未安装，收藏备查

### [jonathanjuliani/skilldeck（JS/TS 工程技能集）](cards/external-collection/jonathanjuliani-skilldeck.md)

- 一句话: 36 个面向 JS/TS、React 与 React Native agent 的工程技能：先探测再决策，设计与工程两条线，共 37 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/jonathanjuliani/skilldeck
- 调用: 未安装，收藏备查

### [jrgilbertson/the-rookery（跨工具 AI 构建实地指南）](cards/external-collection/jrgilbertson-the-rookery.md)

- 一句话: 作者跨工具用 AI 构建的实地指南与实践技能：同一套做法跑在多个 agent 工具上，共 2 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/jrgilbertson/the-rookery
- 调用: 未安装，收藏备查

### [kaankiziltug/logo-design-skill（Logo 设计技能）](cards/external-collection/kaankiziltug-logo-design-skill.md)

- 一句话: 给 AI agent 的 Logo 设计技能：设计原则、流程、SVG 手艺与自检，适配 Claude、Gemini CLI、Codex 等多家 agent。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/kaankiziltug/logo-design-skill
- 调用: 未安装，收藏备查

### [kajisho5/ffmpeg-skill（FFmpeg 视频编辑技能）](cards/external-collection/kajisho5-ffmpeg-skill.md)

- 一句话: 给编码 agent 的本地视频编辑技能：42 个 FFmpeg 工具 + 机器可读契约 + MCP 服务器，剪辑、转码、抽帧都按契约走。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/kajisho5/ffmpeg-skill
- 调用: 未安装，收藏备查

### [kambleakash0/agent-skills（精选 Agent 技能 + 省 token MCP）](cards/external-collection/kambleakash0-agent-skills.md)

- 一句话: 精选的自定义 Agent 技能合集，附省 token 的 MCP 服务器配置，13 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/kambleakash0/agent-skills
- 调用: 未安装，收藏备查

### [karefined-eng/information-is-beautiful-skill（可信图表技能）](cards/external-collection/karefined-eng-information-is-beautiful-skill.md)

- 一句话: 教 agent 做出「好看且可信」的图表——五条可核查法则、一张决策表、25 点审计，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/karefined-eng/information-is-beautiful-skill
- 调用: 未安装，收藏备查

### [kepano/obsidian-skills（Obsidian 技能包）](cards/external-collection/kepano-obsidian-skills.md)

- 一句话: 教 Agent 操作 Obsidian 仓库的技能包：用 Obsidian CLI 读写/搜索笔记、Obsidian 风味 Markdown、Bases 数据库视图、JSON Canvas、网页转 Markdown（Defuddle）、模板渲染（Knap）。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/kepano/obsidian-skills
- 调用: 未安装，收藏备查

### [kerfnotes/skills（简报、逐字稿、职场关系技能）](cards/external-collection/kerfnotes-skills.md)

- 一句话: 给 Codex 与 Claude Code 的技能：Clayprint 做 PowerPoint 简报与 HTML/PDF 报告，Wordprint 整理本地逐字稿，Power Map 分析职场关系与职涯抉择。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/kerfnotes/skills
- 调用: 未安装，收藏备查

### [kjranyone/artcraft-agent-skills（ArtCraft 创意套件技能）](cards/external-collection/kjranyone-artcraft-agent-skills.md)

- 一句话: 驱动 ArtCraft 创意套件的 agent 技能：经 CLI、MCP 与实时 GUI 桥操作 FilmCraft 非编与 EffectCraft 动效/VFX，5 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/kjranyone/artcraft-agent-skills
- 调用: 未安装，收藏备查

### [knowledgeislands/ki-agentic-harness（知识岛 agent 装备库）](cards/external-collection/knowledgeislands-ki-agentic-harness.md)

- 一句话: Knowledge Islands 生态的 agent 装备总库——技能、子 agent、评测与钩子四件套，64 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/knowledgeislands/ki-agentic-harness
- 调用: 未安装，收藏备查

### [konlu/story-studio（中文历史人物配音视频技能）](cards/external-collection/konlu-story-studio.md)

- 一句话: 从选题到剪映草稿的一站式 AI 短视频内容创作技能：中文历史人物配音视频，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/konlu/story-studio
- 调用: 未安装，收藏备查

### [krillinai/OpenCreator（AI 创作工作台技能）](cards/external-collection/krillinai-opencreator.md)

- 一句话: 开源 AI 创作工作台自带的技能：视频下载、翻译配音、成片、封面、字幕、TTS，15 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/krillinai/OpenCreator
- 调用: 未安装，收藏备查

### [kubersharmax/amda-skill（AI 输出要不要人工复核的分流技能）](cards/external-collection/kubersharmax-amda-skill.md)

- 一句话: 告诉你哪些 AI 输出需要人工复核、哪些不用：把营销与 GTM 决策按治理强度分进三档，共 2 个 SKILL.md。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/kubersharmax/amda-skill
- 调用: 未安装，收藏备查

### [kumodeck/game-studio（Web 游戏关卡编辑器技能）](cards/external-collection/kumodeck-game-studio.md)

- 一句话: 给 AI 做的网页游戏配一个免费关卡编辑器：three.js、Phaser、PixiJS 与 Godot 网页游戏，拖东西、让 AI 改、点保存，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/kumodeck/game-studio
- 调用: 未安装，收藏备查

### [latent-spaces/brag（项目启动视频技能）](cards/external-collection/latent-spaces-brag.md)

- 一句话: 刚做完的项目一句话变成可分享的短启动视频，2 个 SKILL.md（完整版 + 精简版）。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/latent-spaces/brag
- 调用: 未安装，收藏备查

### [lawson2019/agent-task-takeover（Agent 任务接管技能）](cards/external-collection/lawson2019-agent-task-takeover.md)

- 一句话: 让 agent 接管任务的技能：根目录 1 个 SKILL.md，仓库未写简介，以 SKILL.md 本体为准。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/lawson2019/agent-task-takeover
- 调用: 未安装，收藏备查

### [lemomo-ai/lemo-opuscar（代码化电影风格工具箱）](cards/external-collection/lemomo-ai-lemo-opuscar.md)

- 一句话: 给 Claude Code 的代码化电影风格工具箱：66 套开箱即用的影片风格，也可自定风格，2 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/lemomo-ai/lemo-opuscar
- 调用: 未安装，收藏备查

### [llodev/skills（Agent 技能合集）](cards/external-collection/llodev-skills.md)

- 一句话: Agent 技能合集 21 个：TS 的 DDD（DTO、实体、用例、查询）、项目管理任务（Jira、Asana、Linear、Notion）与学习摘要等。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/llodev/skills
- 调用: 未安装，收藏备查

### [lmxcode/infocard-video（信息卡短视频流水线）](cards/external-collection/lmxcode-infocard-video.md)

- 一句话: 信息卡短视频全自动流水线：口播 TTS + HTML/CSS 信息卡渲染 + BGM + 字幕，一条 60s 成片现金成本约 0.2 元。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/lmxcode/infocard-video
- 调用: 未安装，收藏备查

### [luizguilherme5/claude-delegation-skills（委派给本地 Claude 的技能）](cards/external-collection/luizguilherme5-claude-delegation-skills.md)

- 一句话: 让 Codex/Cursor/OpenCode 等终端 agent 把工程活委派给本地 Claude Code CLI，带受限权限与会话续跑，2 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/luizguilherme5/claude-delegation-skills
- 调用: 未安装，收藏备查

### [lzhs1995/multi-agent-collaboration（cmux 多 agent 协同）](cards/external-collection/lzhs1995-multi-agent-collaboration.md)

- 一句话: 在 macOS cmux 里协调多个带上下文的 CLI agent——作用域任务包、认证确认、证据回调、评审关卡，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/lzhs1995/multi-agent-collaboration
- 调用: 未安装，收藏备查

### [magnus919/agent-skills（精选 Agent 技能合集）](cards/external-collection/magnus919-agent-skills.md)

- 一句话: 面向 Hermes 等 agent 框架的精选技能合集：精算风险建模、ADR 写作、agent 评审与可观测性、API 设计演进等，共 191 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/magnus919/agent-skills
- 调用: 未安装，收藏备查

### [markfulton/luck-accelerator（本周该见谁的技能）](cards/external-collection/markfulton-luck-accelerator.md)

- 一句话: 每周找出值得见的人、活动与社群，写好第一条消息，放进你自己的 luck dashboard，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/markfulton/luck-accelerator
- 调用: 未安装，收藏备查

### [markksantos/caption-checker（字幕合规检查技能）](cards/external-collection/markksantos-caption-checker.md)

- 一句话: 按 Netflix、BBC 与 DCMP 字幕规范检查 SRT/WebVTT 字幕：语速、行长、行数、时长、间隔与重叠，3 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/markksantos/caption-checker
- 调用: 未安装，收藏备查

### [mattpocock/skills（给真实工程师的技能集）](cards/external-collection/mattpocock-skills.md)

- 一句话: Matt Pocock 每天自用的工程技能——对齐先问透（grill-me）、TDD、查 bug、领域建模、代码评审，38 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/mattpocock/skills
- 调用: 未安装，收藏备查

### [maxg-agency/skills（小型产品构建技能集）](cards/external-collection/maxg-agency-skills.md)

- 一句话: 小而自包含的产品构建技能集——Claude Code 技能加给 ChatGPT 的纯提示词。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/maxg-agency/skills
- 调用: 未安装，收藏备查

### [meshy-dev/meshy-3d-agent（Meshy AI 3D 生成技能）](cards/external-collection/meshy-dev-meshy-3d-agent.md)

- 一句话: Meshy AI 3D 生成平台的 agent 技能：3D 生成、3D 打印与 OpenClaw 集成，共 3 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/meshy-dev/meshy-3d-agent
- 调用: 未安装，收藏备查

### [meshy-dev/meshy-dsh（Meshy 3D 生成与打印技能，DeepSeek Harness 版）](cards/external-collection/meshy-dev-meshy-dsh.md)

- 一句话: Meshy 3D 生成与 3D 打印技能的 DeepSeek Harness（dsh）版：生成与打印各一，共 2 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/meshy-dev/meshy-dsh
- 调用: 未安装，收藏备查

### [michael-denyer/pstack-claude（Poteto 技能栈的 Claude 移植）](cards/external-collection/michael-denyer-pstack-claude.md)

- 一句话: Poteto pstack 技能栈的 Claude Code / Codex / Copilot / Gemini 等多 harness 移植：严格的 agent 工作流与 Cursor 原语对照，共 68 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/michael-denyer/pstack-claude
- 调用: 未安装，收藏备查

### [mileson/chaojifeng-video-design（超级峰的视频设计方法论）](cards/external-collection/mileson-chaojifeng-video-design.md)

- 一句话: 面向 AI Agent 的视频设计方法论技能：从导演意图到分镜、声画节奏、制作与交付验收，覆盖知识讲解、产品演示、音乐视觉等 8 类视频任务。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/mileson/chaojifeng-video-design
- 调用: 「用 chaojifeng-video-design 做一期关于 XX 的概念知识科普视频」

### [morluto/rea（用 agent 逆向任何东西）](cards/external-collection/morluto-rea.md)

- 一句话: 用 agent 逆向任何东西的技能——从应用行为一路深入到原生二进制，5 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/morluto/rea
- 调用: 未安装，收藏备查

### [muse-skills（300 个 Muse 用法合集）](cards/external-collection/muse-skills-jasonbitsmith.md)

- 一句话: 社区整理的 Muse 使用技巧合集，约 300 条，当作灵感库翻。
- 来源: 外部
- 许可: 见上游仓库
- 位置: https://github.com/jasonbitsmith/muse-skills （本地克隆在个人档案馆「外部收藏」分区）
- 调用: 「在外部收藏里找 XX 用法」

### [muzbox1973/arcade-rom-3d-remaster（自有街机 ROM 转 Three.js 3D 重制）](cards/external-collection/muzbox1973-arcade-rom-3d-remaster.md)

- 一句话: 把你自己的 MAME 街机 ROM 做成 Three.js 3D 重制版：原代码不改动运行，音效重制，英/韩双语，根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/muzbox1973/arcade-rom-3d-remaster
- 调用: 未安装，收藏备查

### [nainishshafi/developer-productivity-skills（开发者生产力技能）](cards/external-collection/nainishshafi-developer-productivity-skills.md)

- 一句话: 可复用的开发者生产力技能：读 README、同步 fork、写技能、Python lint、安全扫描等，共 12 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/nainishshafi/developer-productivity-skills
- 调用: 未安装，收藏备查

### [nanaism/yomiyasu（AI 日语润色技能）](cards/external-collection/nanaism-yomiyasu.md)

- 一句话: 把 AI 生成的日语推敲成自然日语的单技能：改掉机器味，保留原意。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/nanaism/yomiyasu
- 调用: 未安装，收藏备查

### [nanocoai/nanoclaw（轻量 OpenClaw 替代）](cards/external-collection/nanocoai-nanoclaw.md)

- 一句话: "A lightweight alternative to OpenClaw that runs in containers" —— agent 框架 + 自带 64 个集成技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/nanocoai/nanoclaw
- 调用: 未安装，收藏备查

### [naorsabag/openhop（交互数据流图技能）](cards/external-collection/naorsabag-openhop.md)

- 一句话: 一个 SKILL.md 让 agent 写出可交互的数据流图 —— local-first 无遥测，支持 Claude Code/Cursor/Codex 等 11+ 客户端。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/naorsabag/openhop
- 调用: 未安装，收藏备查

### [nathankim0/ssul（韩语拟人社交帖技能）](cards/external-collection/nathankim0-ssul.md)

- 一句话: 写出像真人而不是 AI 的韩语社交帖子，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/nathankim0/ssul
- 调用: 未安装，收藏备查

### [netresearch/agent-rules-skill（AGENTS.md 生成技能）](cards/external-collection/netresearch-agent-rules-skill.md)

- 一句话: 按 agents.md 约定为项目生成 AGENTS.md 文件的单技能，Claude Code 兼容，1 个 SKILL.md。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/netresearch/agent-rules-skill
- 调用: 未安装，收藏备查

### [newsbubbles/ismail（高带宽 Agent 界面）](cards/external-collection/newsbubbles-ismail.md)

- 一句话: 高带宽 agent 界面 Ismail，含 Agentic DAW 与 Agentic VR 舞台，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/newsbubbles/ismail
- 调用: 未安装，收藏备查

### [nexu-io/html-anything（Agentic HTML 编辑器模板技能）](cards/external-collection/nexu-io-html-anything.md)

- 一句话: Agentic HTML 编辑器自带的模板技能库：文章、杂志、信息图、卡片、看板、数据报告、课程 deck 等方向，共 81 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/nexu-io/html-anything
- 调用: 未安装，收藏备查

### [nexu-io/open-design（协作式 AI 设计工作台技能）](cards/external-collection/nexu-io-open-design.md)

- 一句话: 「The 1st Collaborative AI Design Agent Workspace」——local-first 开源设计 agent 工作台，仓内 552 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/nexu-io/open-design
- 调用: 未安装，收藏备查

### [nidhinjs/prompt-master（提示词写作技能）](cards/external-collection/nidhinjs-prompt-master.md)

- 一句话: 给任意 AI 工具写准确提示词的 Claude 技能：根目录 1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/nidhinjs/prompt-master
- 调用: 未安装，收藏备查

### [nightly-labs/openbot（本地优先的多智能体桌面工作台）](cards/external-collection/nightly-labs-openbot.md)

- 一句话: 本地优先的桌面工作台，给每个 AI 队友一个独立工作区和会话，可跑 Codex、Claude、Grok 等多个 agent 并让它们互相协作。
- 来源: 外部
- 许可: PolyForm Noncommercial 1.0.0（非商业许可；商业使用需另向版权方申请，0.1.11 及之前版本为 Apache-2.0）
- 位置: https://github.com/nightly-labs/openbot
- 调用: 未安装，收藏备查

### [obra/superpowers（完整开发方法论技能框架）](cards/external-collection/obra-superpowers.md)

- 一句话: 一套完整软件开发方法论的技能框架——先头脑风暴对齐、再写计划、子 agent 分工执行、TDD 与评审兜底，15 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/obra/superpowers
- 调用: 未安装，收藏备查

### [paperclipai/paperclip（Agent 管理应用的技能包）](cards/external-collection/paperclipai-paperclip.md)

- 一句话: 开源的 agent 管理应用（"everyone uses to manage agents at work"），仓内自带 82 个 SKILL.md——产品技能加 skill 分发结构。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/paperclipai/paperclip
- 调用: 未安装，收藏备查

### [patch-gg/pixelfx（244 个代码像素风特效 + 出图技能）](cards/external-collection/patch-gg-pixelfx.md)

- 一句话: 244 个代码绘制的像素风特效（每种都是一小段代码），附一个 Claude Code 技能帮你生成自己的特效、导出精灵表，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/patch-gg/pixelfx
- 调用: 未安装，收藏备查

### [pbakaus/impeccable（设计词汇技能）](cards/external-collection/pbakaus-impeccable.md)

- 一句话: 给 coding agent 的设计词汇技能：用一套可复用的设计语言把关 polish 与大胆度，1 个技能适配 26 个 harness。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/pbakaus/impeccable
- 调用: 未安装，收藏备查

### [phuryn/pm-skills（产品经理技能市场）](cards/external-collection/phuryn-pm-skills.md)

- 一句话: 产品经理的 agentic 技能市场：PRD、OKR、AB 测试、发布、复盘、路线图等 69 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/phuryn/pm-skills
- 调用: 未安装，收藏备查

### [pierpont-morgan/gcp-free-vps-skill（GCP 永久免费 VPS 部署）](cards/external-collection/pierpont-morgan-gcp-free-vps-skill.md)

- 一句话: 一份实测口径的 GCP Always Free VPS 全流程部署技能：先领 300 美元试用金，再建 e2-micro 免费机，配预算告警、CDN 出站屏蔽、流量只限流、Debian 换源与 dae 出站。
- 来源: 外部
- 许可: 未标注（仓库无 LICENSE 文件，GitHub API license 为空）
- 位置: https://github.com/pierpont-morgan/gcp-free-vps-skill
- 调用: 未安装，收藏备查

### [pku2319/project-template（新项目脚手架技能）](cards/external-collection/pku2319-project-template.md)

- 一句话: 用 agent 技能创建新项目的脚手架：可交付技能 1 个，另带 1 个模板内安装技能复本。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/pku2319/project-template
- 调用: 未安装，收藏备查

### [product-on-purpose/critique-skills（按量规出机器可读评审）](cards/external-collection/product-on-purpose-critique-skills.md)

- 一句话: 按评分量规做评审的技能包，输出机器可解析的结论而非自由发挥的意见，8 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/product-on-purpose/critique-skills
- 调用: 未安装，收藏备查

### [programmablehq/PROGRAMMABLE（Uniswap v4 启动模型技能）](cards/external-collection/programmablehq-programmable.md)

- 一句话: 以太坊上 Uniswap v4 启动模型基础设施附带的 hook 构建技能，单技能。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/programmablehq/PROGRAMMABLE
- 调用: 未安装，收藏备查

### [qjzzsky/lyric-onset-montage（歌词起音剪辑技能）](cards/external-collection/qjzzsky-lyric-onset-montage.md)

- 一句话: 按唱词的实测起音点切画面——不是卡节拍、不是卡字幕，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/qjzzsky/lyric-onset-montage
- 调用: 未安装，收藏备查

### [ramboz/jig（跨平台工程技能集）](cards/external-collection/ramboz-jig.md)

- 一句话: 跨 Claude 与 Codex 的工程技能集：同一批技能按 harness 各放一份，树内 80 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/ramboz/jig
- 调用: 未安装，收藏备查

### [reactive-resume/reactive-resume（简历与求职技能插件集）](cards/external-collection/reactive-resume-reactive-resume.md)

- 一句话: 开源简历生成器的 Claude 插件技能集：按职业写简历、改子弹句、量身定制、模拟面试与 offer 谈判，共 32 个可交付技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/reactive-resume/reactive-resume
- 调用: 未安装，收藏备查

### [rediumvex/meta-facebook-ads-optimizer-claude（广告诊断技能）](cards/external-collection/rediumvex-meta-facebook-ads-optimizer-claude.md)

- 一句话: 单技能：诊断"广告烧钱不转化"——投放审计、交付停滞、样本量规则、像素核查五步诊断流程，附完整 teardown 实战案例。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/rediumvex/meta-facebook-ads-optimizer-claude
- 调用: 未安装，收藏备查

### [remote-controlled-man/skillfit（衡量技能是否真提升任务）](cards/external-collection/remote-controlled-man-skillfit.md)

- 一句话: 给技能本身做跑分：衡量 AI 编码 agent 的 Skills、规则与 MCP 配置是否真的提升了你的任务效果，而不是凭感觉装一堆。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/remote-controlled-man/skillfit
- 调用: 未安装，收藏备查

### [reticlehq/reticle（让 Agent 理解自己写的代码）](cards/external-collection/reticlehq-reticle.md)

- 一句话: 针对「agent 能写代码却不理解自己构建了什么」的技能包，22 个 SKILL.md。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/reticlehq/reticle
- 调用: 未安装，收藏备查

### [rogerchappel/launchclip（启动视频与开源宣发包技能）](cards/external-collection/rogerchappel-launchclip.md)

- 一句话: 做可审阅的启动视频与开源宣发包：角色设计、视频生成、发布文案，树内 7 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/rogerchappel/launchclip
- 调用: 未安装，收藏备查

### [rollingedition/agent-skills（Rolling Edition 图书转 Agent 技能）](cards/external-collection/rollingedition-agent-skills.md)

- 一句话: 把 Rolling Edition 的图书做成 agent 技能：商业智能、数据治理、MCP 实战、开放表格式、搜索相关性、时序预测，共 6 个可交付技能。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/rollingedition/agent-skills
- 调用: 未安装，收藏备查

### [runxhq/runx（带治理的技能运行时）](cards/external-collection/runxhq-runx.md)

- 一句话: 把技能当可治理运行时跑——技能可互相调用、权限显式收窄、每次执行留可验证凭证，92 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/runxhq/runx
- 调用: 未安装，收藏备查

### [sageadvicellc/bowerloom（Harness 与 Agent 环境管理）](cards/external-collection/sageadvicellc-bowerloom.md)

- 一句话: 用 CLI + App 管 harness 与 agent 环境：工厂式交付四件套（接单、交付、交接、评审）加 wiki-keeper 笔记技能与 labs-to-blog 配方，共 12 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/sageadvicellc/bowerloom
- 调用: 未安装，收藏备查

### [say8425/SimpleKorean（易懂韩语写作技能）](cards/external-collection/say8425-simplekorean.md)

- 一句话: 让 LLM 把技术文档和聊天回答写成简单易懂的韩语，源自 SimpleEnglish（ASD-STE100）的韩语派生项目。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/say8425/SimpleKorean
- 调用: 未安装，收藏备查

### [shadcn/improve（最强模型审计代码库、给便宜模型写计划）](cards/external-collection/shadcn-improve.md)

- 一句话: 用最强的模型审计代码库、写出可执行的改进计划，再交给便宜的模型去执行：严格只读审计，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/shadcn/improve
- 调用: 未安装，收藏备查

### [showheyohtaki/motion-prompt（动作词典技能）](cards/external-collection/showheyohtaki-motion-prompt.md)

- 一句话: 192 个动效、镜头、UI、网页与照片效果的动作词典：每个名字配一段动起来的示例，知道效果叫什么、不知道怎么做时查它，单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/showheyohtaki/motion-prompt
- 调用: 未安装，收藏备查

### [shrek-abaper/sap-engineering-skill（SAP 工程技能）](cards/external-collection/shrek-abaper-sap-engineering-skill.md)

- 一句话: 面向 SAP 的原子化工程技能：ABAP 代码与业务逻辑分析、源码读写、单元测试与 Dump 诊断、实验调试、代码评审与传输就绪检查，4 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/shrek-abaper/sap-engineering-skill
- 调用: 未安装，收藏备查

### [sickn33/agentic-awesome-skills（2750+ 技能巨型合集）](cards/external-collection/sickn33-agentic-awesome-skills.md)

- 一句话: 自称 2750+ agentic 技能的本地控制平面：目录发现、agent 自选、栈校验与规划，仓内实测 8,589 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/sickn33/agentic-awesome-skills
- 调用: 未安装，收藏备查

### [skeptrunedev/call4me（编码 agent 打电话）](cards/external-collection/skeptrunedev-call4me.md)

- 一句话: 让编码 agent 替你打电话：基于 Telnyx + OpenAI GPT-Live 的 MCP 工具，agent 能直接拨号沟通。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/skeptrunedev/call4me
- 调用: 未安装，收藏备查

### [skrodahl/delegate-to-local（本地模型写代码）](cards/external-collection/skrodahl-delegate-to-local.md)

- 一句话: Claude 负责规划和评审，本地模型负责写代码的分工技能，1 个 SKILL.md。
- 来源: 外部
- 许可: BSD-3-Clause
- 位置: https://github.com/skrodahl/delegate-to-local
- 调用: 未安装，收藏备查

### [soul0710/story-narration-skills（长叙事口播视频脚本）](cards/external-collection/soul0710-story-narration-skills.md)

- 一句话: 写 30–120+ 分钟长叙事口播视频脚本的 7 个技能：立意、大纲、圣经设定、写作、分镜、审校、成片工作室。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/soul0710/story-narration-skills
- 调用: 未安装，收藏备查

### [ssinder/bioinformatics-agent-skills（计算生物学技能包）](cards/external-collection/ssinder-bioinformatics-agent-skills.md)

- 一句话: 计算生物学 agent 技能：RNA-seq、单细胞、蛋白质结构、分子动力学、肽设计，17 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/ssinder/bioinformatics-agent-skills
- 调用: 未安装，收藏备查

### [st666xiao/claude-relay（多模型接力流程）](cards/external-collection/st666xiao-claude-relay.md)

- 一句话: Opus 指挥、干活模型执行、Haiku 验收、Sonnet 审查——靠流程约束分工，不靠模型自觉的多模型接力技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/st666xiao/claude-relay
- 调用: 未安装，收藏备查

### [stancsz/northstar（委派式 AI 团队技能）](cards/external-collection/stancsz-northstar.md)

- 一句话: 给 AI 团队下使命、让它自己担决策、你只验结果——六个协同技能管授权、验收与复盘，6 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/stancsz/northstar
- 调用: 未安装，收藏备查

### [starslingdev/skills（Agent 原生 CI 技能）](cards/external-collection/starslingdev-skills.md)

- 一句话: StarSling 的 agent 原生 CI 技能：给 CI 打分、加固安全、提速流水线，共 5 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/starslingdev/skills
- 调用: 未安装，收藏备查

### [tamnguyendinh/Anvien（代码智能 MCP 技能）](cards/external-collection/tamnguyendinh-anvien.md)

- 一句话: 本地 MCP 代码智能工具的技能包：定位问题、找文件符号、验证调用链，仓内 78 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/tamnguyendinh/Anvien
- 调用: 未安装，收藏备查

### [techhorizonlabs/gearlist（来源核查过的 MCP 与技能清单）](cards/external-collection/techhorizonlabs-gearlist.md)

- 一句话: 来源核查过的 MCP 服务器、agent 技能与工具清单，附访问说明，6 个 SKILL.md。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/techhorizonlabs/gearlist
- 调用: 未安装，收藏备查

### [teng-lin/notebooklm-py（NotebookLM 客户端技能）](cards/external-collection/teng-lin-notebooklm-py.md)

- 一句话: NotebookLM 的 Python 客户端自带 agent 技能：根目录 1 个 SKILL.md，让 agent 能调用 NotebookLM 能力。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/teng-lin/notebooklm-py
- 调用: 未安装，收藏备查

### [thedotmack/claude-mem（跨会话持久记忆）](cards/external-collection/thedotmack-claude-mem.md)

- 一句话: 让 agent 在会话间持久化上下文：记录每个 session 的行为，AI 压缩后在未来 session 注入相关上下文，含 41 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/thedotmack/claude-mem
- 调用: 未安装，收藏备查

### [titanwings/distilly（思维蒸馏成技能）](cards/external-collection/titanwings-distilly.md)

- 一句话: 把「他们是怎么思考的」蒸馏成可复用的 Skills（默认分支就叫 dot-skill）。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/titanwings/distilly
- 调用: 未安装，收藏备查

### [trevhud/rote（把技能编译成确定性流水线）](cards/external-collection/trevhud-rote.md)

- 一句话: 把 AI agent 技能编译成便宜、快速、确定性的流水线，运行时不需要 LLM 参与，22 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/trevhud/rote
- 调用: 未安装，收藏备查

### [tt-a1i/archify（交互式图解技能）](cards/external-collection/tt-a1i-archify.md)

- 一句话: 把任何想法、计划或代码库变成漂亮交互式图表的 agent skill，面向 Claude Code / Codex 等，5 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/tt-a1i/archify
- 调用: 未安装，收藏备查

### [ueberdosis/tiptap（Tiptap 编辑器集成技能）](cards/external-collection/ueberdosis-tiptap.md)

- 一句话: Tiptap 无头富文本编辑器框架仓内附带的 2 个 agent 技能：tiptap 集成技能与 create-pr，共 2 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/ueberdosis/tiptap
- 调用: 未安装，收藏备查

### [vargHQ/skills（73 个 AI 视频技能）](cards/external-collection/varghq-skills.md)

- 一句话: 73 个 AI 视频技能：视频脚本、预演、分镜、配音、音效、评审等，覆盖 Claude Code、Codex、Grok、Cursor 等多个 agent。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/vargHQ/skills
- 调用: 未安装，收藏备查

### [vercel-labs/agent-browser（Agent 浏览器技能）](cards/external-collection/vercel-labs-agent-browser.md)

- 一句话: Vercel 出品的 agent 浏览器自动化 CLI 附带技能：浏览器操作、沙箱、部署与 WebMCP 生成，共 11 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/vercel-labs/agent-browser
- 调用: 未安装，收藏备查

### [vercel-labs/skills（npx skills 工具与找技能技能）](cards/external-collection/vercel-labs-skills.md)

- 一句话: 开源 agent 技能工具 `npx skills` 本体：装技能的命令行工具，仓内附带 1 个可交付技能 find-skills（帮你找技能）与内部自动化技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/vercel-labs/skills
- 调用: 未安装，收藏备查

### [virgiliojr94/book-to-skill（书转技能）](cards/external-collection/virgiliojr94-book-to-skill.md)

- 一句话: 把技术书（PDF / EPUB / DOCX / HTML / Markdown / 纯文本 / RTF / MOBI）转成 Claude 系 Agent 技能——抽的是框架、心智模型、原则、技术和反模式，不是摘要。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/virgiliojr94/book-to-skill
- 调用: 未安装，收藏备查

### [voidd0/apify-skills（Apify 数据采集技能集）](cards/external-collection/voidd0-apify-skills.md)

- 一句话: 给 Claude Code、Codex、Copilot 与 Cursor 的 Apify 数据技能：广告库、应用商店数据、电商、招聘、房产、研报新闻等，共 11 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/voidd0/apify-skills
- 调用: 未安装，收藏备查

### [wanshuiyin/Auto-claude-code-research-in-sleep（ARIS 自主 ML 研究技能）](cards/external-collection/wanshuiyin-auto-claude-code-research-in-sleep.md)

- 一句话: ARIS：睡觉时让 agent 自己做 ML 研究——纯 Markdown 技能，跨模型互审、点子发现、实验自动化，共 197 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
- 调用: 未安装，收藏备查

### [wheakerd/axiom（Codex/Claude Code 工作流技能）](cards/external-collection/wheakerd-axiom.md)

- 一句话: 面向 Codex 与 Claude Code 的聚焦型工作流技能：把请求变成清晰可执行的任务，共 14 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/wheakerd/axiom
- 调用: 未安装，收藏备查

### [whozghiar/opengoal-modding-kb（OpenGOAL Modding 知识技能库）](cards/external-collection/whozghiar-opengoal-modding-kb.md)

- 一句话: 经核验的 OpenGOAL modding 知识，做成 Agent Skills：关卡编辑器、Remotion 视频、文档与写作，共 22 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/whozghiar/opengoal-modding-kb
- 调用: 未安装，收藏备查

### [why20261/douyin-competitor-radar（抖音竞品雷达技能）](cards/external-collection/why20261-douyin-competitor-radar.md)

- 一句话: 对比品牌在抖音的内容表现、互动数据与讨论趋势，输出差异、证据与可执行机会的竞品分析单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/why20261/douyin-competitor-radar
- 调用: 未安装，收藏备查

### [why20261/douyin-video-words（抖音视频文案提取）](cards/external-collection/why20261-douyin-video-words.md)

- 一句话: 输入抖音视频链接，用千问 LLM 做智能语音转写，把视频文案提取出来，支持普通话、粤语等方言及外语。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/why20261/douyin-video-words
- 调用: 未安装，收藏备查

### [why20261/kuaishou-opportunity-research（快手机会研究）](cards/external-collection/why20261-kuaishou-opportunity-research.md)

- 一句话: 研究快手搜索结果、作品结构、达人数据和用户反馈，筛选值得继续验证的机会，服务快手选题、增长与用户痛点分析。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/why20261/kuaishou-opportunity-research
- 调用: 未安装，收藏备查

### [wshobson/agents（多 harness 插件市场）](cards/external-collection/wshobson-agents.md)

- 一句话: 面向多 harness 的 agentic 插件市场（Claude Code / Codex / Cursor / OpenCode / Copilot / Antigravity / Pi），含 185 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/wshobson/agents
- 调用: 未安装，收藏备查

### [yikart/AiToEarn（AI 内容变现平台技能插件）](cards/external-collection/yikart-aitoearn.md)

- 一句话: 「用 AI 赚钱」的内容生产平台附带 Claude 插件技能：视频生成、剪辑、配音、图片、频道发布等 14 个技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/yikart/AiToEarn
- 调用: 未安装，收藏备查

### [yusufkaraaslan/Skill_Seekers（文档转技能技能）](cards/external-collection/yusufkaraaslan-skill-seekers.md)

- 一句话: 把文档站、GitHub 仓库、PDF 转成 Claude 技能，带自动冲突检测，2 个可交付技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/yusufkaraaslan/Skill_Seekers
- 调用: 未安装，收藏备查

### [zenstory-ai/drama-skills（AI 短剧/漫剧创作技能合集）](cards/external-collection/zenstory-ai-drama-skills.md)

- 一句话: 开源 AI 短剧/漫剧创作技能合集：剧本、角色资产、分镜、图片/视频提示词、审查，适配 Claude Code 与 Codex，共 12 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/zenstory-ai/drama-skills
- 调用: 未安装，收藏备查

### [zenstory-ai/oh-story-claudecode（中文网文写作技能）](cards/external-collection/zenstory-ai-oh-story-claudecode.md)

- 一句话: 给 Claude Code / Codex / OpenCode 写中文网文的 agent 技能包：长短篇分析、扫描、写作、审校、封面、导入与发布。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/zenstory-ai/oh-story-claudecode
- 调用: 未安装，收藏备查

### [zhanghao123vip/ai-manju-skills（21 题材 AI 漫剧全流程技能）](cards/external-collection/zhanghao123vip-ai-manju-skills.md)

- 一句话: 21 个题材的 AI 漫剧全流程技能：一句点子生成企划案、资产图提示词、分集剧本、分镜与视频提示词，适配 Claude Code、WorkBuddy、DeepSeek。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/zhanghao123vip/ai-manju-skills
- 调用: 未安装，收藏备查

### [zhuyansen/awesome-claude-video-skills（视频技能合集）](cards/external-collection/zhuyansen-awesome-claude-video-skills.md)

- 一句话: 专收「让编程 agent 做视频」的开源 skills 与工具包的清单型合集，带预览图，中文作者维护。
- 来源: 外部
- 许可: 见上游（API 标注 NOASSERTION）
- 位置: https://github.com/zhuyansen/awesome-claude-video-skills
- 调用: 未安装，收藏备查
