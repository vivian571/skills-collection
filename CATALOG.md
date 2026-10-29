# CATALOG · 技能总索引

共 120 张卡，7 个分类。本文件由 `scripts/build_catalog.py` 自动生成，不要手改。

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

### [AIPMAndy/ClearSkill（磁盘清理决策技能）](cards/external-collection/aipmandy-clearskill.md)

- 一句话: 帮 Claude Code 做安全的磁盘清理决策——先判断能不能删、再决定怎么删的单技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/AIPMAndy/ClearSkill
- 调用: 未安装，收藏备查

### [Alisa0808/vox-director（Vox 拼贴讲解视频技能）](cards/external-collection/alisa0808-vox-director.md)

- 一句话: 把一个主题自动做成 Vox 风纸拼贴讲解/广告视频的 agent skill，全流程跑在 Atlas Cloud + ffmpeg 上。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/Alisa0808/vox-director
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

### [JasonHMY/personal-finance-visualizer（本地交互式财务报告）](cards/external-collection/jasonhmy-personal-finance-visualizer.md)

- 一句话: 让 agent 把财务数据做成本地交互式报告：圆形图、交易钻取，中英双语，记忆优先处理。
- 来源: 外部
- 许可: MIT-0
- 位置: https://github.com/JasonHMY/personal-finance-visualizer
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

### [K-Dense-AI/scientific-agent-skills（科学技能库）](cards/external-collection/k-dense-scientific-agent-skills.md)

- 一句话: 把 AI agent 变成科研助手的技能库，177 个 SKILL.md，是本批单库体量最大的一个。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/K-Dense-AI/scientific-agent-skills
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

### [MSKazemi/reachweaver（社媒排期技能）](cards/external-collection/mskazemi-reachweaver.md)

- 一句话: Claude Code 社媒技能：证据驱动排期、审批优先发布、发布工作流与复盘分析，2 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/MSKazemi/reachweaver
- 调用: 未安装，收藏备查

### [NevaMind-AI/memU（跨 Agent 个人记忆）](cards/external-collection/nevamind-ai-memu.md)

- 一句话: 跨 agent 的个人记忆技能，让不同 agent 共享同一份个人记忆，1 个 SKILL.md。
- 来源: 外部
- 许可: NOASSERTION（仓库未声明标准 SPDX 许可）
- 位置: https://github.com/NevaMind-AI/memU
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

### [SHARPLEE00/lookbk-skills（视频/幻灯片/图片/网页技能）](cards/external-collection/sharplee00-lookbk-skills.md)

- 一句话: 给 Claude Code、Codex、Cursor 的免费技能：做视频、幻灯片、图片和网页，7 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/SHARPLEE00/lookbk-skills
- 调用: 未安装，收藏备查

### [SupercmoHQ/superCMO-skills（AI 营销官技能包）](cards/external-collection/supercmohq-supercmo-skills.md)

- 一句话: 把 Claude/Cursor/Codex 变成 AI CMO —— 端到端营销 campaign 技能包：UGC 视频、广告视频、产品摄影等，共 23 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/SupercmoHQ/superCMO-skills
- 调用: 未安装，收藏备查

### [VoltAgent/awesome-agent-skills（1000+ 技能清单）](cards/external-collection/voltagent-awesome-agent-skills.md)

- 一句话: 清单型合集：自称收录 1000+ 来自官方团队与社区的 agent skill（兼容 Claude Code / Codex / Gemini CLI / Cursor 等），仓内只有清单没有 SKILL.md 本体。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/VoltAgent/awesome-agent-skills
- 调用: 未安装，收藏备查

### [WenyuChiou/ai-research-skills（科研工作流技能目录·清单）](cards/external-collection/wenyuchiou-ai-research-skills.md)

- 一句话: 科研工作流技能目录：文献综述、研究设计、项目记忆、稿件写作、跨 agent 分派 —— 以 catalog/skills.yml 形式收录的清单型合集（仓内无 SKILL.md 本体）。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/WenyuChiou/ai-research-skills
- 调用: 未安装，收藏备查

### [aaron-he-zhu/aaron-marketing-skills（120 个营销技能）](cards/external-collection/aaron-he-zhu-aaron-marketing-skills.md)

- 一句话: 一支可安装的 AI 营销团队——叙事、SEO/GEO、社媒、邮件、付费广告、网红、发布 7 大学科共 120 个技能。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/aaron-he-zhu/aaron-marketing-skills
- 调用: 未安装，收藏备查

### [addyosmani/agent-skills（工程技能库）](cards/external-collection/addyosmani-agent-skills.md)

- 一句话: Addy Osmani 出品的生产级工程技能库，25 个 SKILL.md，覆盖 API 设计、代码审查、CI/CD 等。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/addyosmani/agent-skills
- 调用: 未安装，收藏备查

### [aiskillstore/marketplace（技能市场）](cards/external-collection/aiskillstore-marketplace.md)

- 一句话: 技能市场仓库，树内含 6,183 个 SKILL.md，规模异常大，疑为批量收录。
- 来源: 外部
- 许可: 未标注
- 位置: https://github.com/aiskillstore/marketplace
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

### [anthropics/skills（Anthropic 官方技能库）](cards/external-collection/anthropics-skills.md)

- 一句话: Anthropic 官方的 Agent Skills 仓库，skills/ 目录下是一批官方出品的 SKILL.md，可当写法范本。
- 来源: 外部
- 许可: 见仓库内各技能自带 LICENSE（API 未标注统一 SPDX）
- 位置: https://github.com/anthropics/skills
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

### [blader/humanizer（去 AI 味改写技能）](cards/external-collection/blader-humanizer.md)

- 一句话: 去掉文本里的 AI 生成痕迹、改写成自然人味的 agent 技能，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/blader/humanizer
- 调用: 未安装，收藏备查

### [career-ops-hq/career-ops（AI 求职 agent 技能）](cards/external-collection/career-ops-hq-career-ops.md)

- 一句话: 开源 AI 求职 agent：扫招聘版、按 CV 逐个 1–5 分打分再决定投不投——同一技能适配 7 个 harness，7 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/career-ops-hq/career-ops
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

### [dereknex/immune-brain（Agent 免疫大脑）](cards/external-collection/dereknex-immune-brain.md)

- 一句话: 给 agent 的免疫式工作流技能：澄清、起草、驱动、修 PR、精简文档与测试、复盘，共 9 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/dereknex/immune-brain
- 调用: 未安装，收藏备查

### [e1dred/agent-skills（桌面应用驱动技能）](cards/external-collection/e1dred-agent-skills.md)

- 一句话: 让 agent 动手操作桌面应用的技能：CAD、演示文稿、办公套件、图片处理，共 7 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/e1dred/agent-skills
- 调用: 未安装，收藏备查

### [eternityspring/shuohao-skills（AI 短剧制作技能集）](cards/external-collection/eternityspring-shuohao-skills.md)

- 一句话: AI 短剧制作的 7 个技能：小说改编大纲、角色设定、角色参考图、场景道具设定、剧本、分镜场位、分镜，一路做到可投产的分镜包。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/eternityspring/shuohao-skills
- 调用: 未安装，收藏备查

### [f-o-x11/deed-page-skill（deed.page 发布技能）](cards/external-collection/f-o-x11-deed-page-skill.md)

- 一句话: 一个 curl 把文件或文件夹发布成永久网址的 agent 技能，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/f-o-x11/deed-page-skill
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

### [gengwg/skills（npx 可装技能集）](cards/external-collection/gengwg-skills.md)

- 一句话: 一组偏运维排障的 agent 技能，可用 npx skills add 安装，35 个 SKILL.md。
- 来源: 外部
- 许可: 未标注（API 未返回 SPDX）
- 位置: https://github.com/gengwg/skills
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

### [knowledgeislands/ki-agentic-harness（知识岛 agent 装备库）](cards/external-collection/knowledgeislands-ki-agentic-harness.md)

- 一句话: Knowledge Islands 生态的 agent 装备总库——技能、子 agent、评测与钩子四件套，64 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/knowledgeislands/ki-agentic-harness
- 调用: 未安装，收藏备查

### [krillinai/OpenCreator（AI 创作工作台技能）](cards/external-collection/krillinai-opencreator.md)

- 一句话: 开源 AI 创作工作台自带的技能：视频下载、翻译配音、成片、封面、字幕、TTS，15 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/krillinai/OpenCreator
- 调用: 未安装，收藏备查

### [latent-spaces/brag（项目启动视频技能）](cards/external-collection/latent-spaces-brag.md)

- 一句话: 刚做完的项目一句话变成可分享的短启动视频，2 个 SKILL.md（完整版 + 精简版）。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/latent-spaces/brag
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

### [newsbubbles/ismail（高带宽 Agent 界面）](cards/external-collection/newsbubbles-ismail.md)

- 一句话: 高带宽 agent 界面 Ismail，含 Agentic DAW 与 Agentic VR 舞台，1 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/newsbubbles/ismail
- 调用: 未安装，收藏备查

### [nexu-io/open-design（协作式 AI 设计工作台技能）](cards/external-collection/nexu-io-open-design.md)

- 一句话: 「The 1st Collaborative AI Design Agent Workspace」——local-first 开源设计 agent 工作台，仓内 552 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/nexu-io/open-design
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

### [pierpont-morgan/gcp-free-vps-skill（GCP 永久免费 VPS 部署）](cards/external-collection/pierpont-morgan-gcp-free-vps-skill.md)

- 一句话: 一份实测口径的 GCP Always Free VPS 全流程部署技能：先领 300 美元试用金，再建 e2-micro 免费机，配预算告警、CDN 出站屏蔽、流量只限流、Debian 换源与 dae 出站。
- 来源: 外部
- 许可: 未标注（仓库无 LICENSE 文件，GitHub API license 为空）
- 位置: https://github.com/pierpont-morgan/gcp-free-vps-skill
- 调用: 未安装，收藏备查

### [product-on-purpose/critique-skills（按量规出机器可读评审）](cards/external-collection/product-on-purpose-critique-skills.md)

- 一句话: 按评分量规做评审的技能包，输出机器可解析的结论而非自由发挥的意见，8 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/product-on-purpose/critique-skills
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

### [runxhq/runx（带治理的技能运行时）](cards/external-collection/runxhq-runx.md)

- 一句话: 把技能当可治理运行时跑——技能可互相调用、权限显式收窄、每次执行留可验证凭证，92 个 SKILL.md。
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/runxhq/runx
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

### [ssinder/bioinformatics-agent-skills（计算生物学技能包）](cards/external-collection/ssinder-bioinformatics-agent-skills.md)

- 一句话: 计算生物学 agent 技能：RNA-seq、单细胞、蛋白质结构、分子动力学、肽设计，17 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/ssinder/bioinformatics-agent-skills
- 调用: 未安装，收藏备查

### [stancsz/northstar（委派式 AI 团队技能）](cards/external-collection/stancsz-northstar.md)

- 一句话: 给 AI 团队下使命、让它自己担决策、你只验结果——六个协同技能管授权、验收与复盘，6 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/stancsz/northstar
- 调用: 未安装，收藏备查

### [tamnguyendinh/Anvien（代码智能 MCP 技能）](cards/external-collection/tamnguyendinh-anvien.md)

- 一句话: 本地 MCP 代码智能工具的技能包：定位问题、找文件符号、验证调用链，仓内 78 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/tamnguyendinh/Anvien
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

### [virgiliojr94/book-to-skill（书转技能）](cards/external-collection/virgiliojr94-book-to-skill.md)

- 一句话: 把技术书（PDF / EPUB / DOCX / HTML / Markdown / 纯文本 / RTF / MOBI）转成 Claude 系 Agent 技能——抽的是框架、心智模型、原则、技术和反模式，不是摘要。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/virgiliojr94/book-to-skill
- 调用: 未安装，收藏备查

### [why20261/douyin-video-words（抖音视频文案提取）](cards/external-collection/why20261-douyin-video-words.md)

- 一句话: 输入抖音视频链接，用千问 LLM 做智能语音转写，把视频文案提取出来，支持普通话、粤语等方言及外语。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/why20261/douyin-video-words
- 调用: 未安装，收藏备查

### [wshobson/agents（多 harness 插件市场）](cards/external-collection/wshobson-agents.md)

- 一句话: 面向多 harness 的 agentic 插件市场（Claude Code / Codex / Cursor / OpenCode / Copilot / Antigravity / Pi），含 185 个 SKILL.md。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/wshobson/agents
- 调用: 未安装，收藏备查

### [yusufkaraaslan/Skill_Seekers（文档转技能技能）](cards/external-collection/yusufkaraaslan-skill-seekers.md)

- 一句话: 把文档站、GitHub 仓库、PDF 转成 Claude 技能，带自动冲突检测，2 个可交付技能。
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/yusufkaraaslan/Skill_Seekers
- 调用: 未安装，收藏备查

### [zhuyansen/awesome-claude-video-skills（视频技能合集）](cards/external-collection/zhuyansen-awesome-claude-video-skills.md)

- 一句话: 专收「让编程 agent 做视频」的开源 skills 与工具包的清单型合集，带预览图，中文作者维护。
- 来源: 外部
- 许可: 见上游（API 标注 NOASSERTION）
- 位置: https://github.com/zhuyansen/awesome-claude-video-skills
- 调用: 未安装，收藏备查
