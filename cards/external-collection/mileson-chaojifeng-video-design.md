# mileson/chaojifeng-video-design（超级峰的视频设计方法论）

- 分类: 外部收藏
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/mileson/chaojifeng-video-design
- 调用: 「用 chaojifeng-video-design 做一期关于 XX 的概念知识科普视频」
- 一句话: 面向 AI Agent 的视频设计方法论技能：从导演意图到分镜、声画节奏、制作与交付验收，覆盖知识讲解、产品演示、音乐视觉等 8 类视频任务。

## 说明

2026-10-29 Vivian 微信推送，嘱「搜集这些技能，并用里面的技能做个知识科普」。验真（2026-10-29，GitHub 一手 + 稀疏克隆核对）：★428，MIT，创建 2026-10-20，根目录有 SKILL.md（仅 1 个 SKILL.md，不是多个独立技能）。

本库实际构成：1 个方法论技能 + 59 套影片风格包（源自 LemoLab · Lemo-Opuscar，已接入统一风格包和中文目录，含样片）+ 7 套基础风格 + 18 类组合配方 + 64 项表达指导 + 12 项基础动效 + 目录/校验脚本（catalog.py、stylepacks.py、validate_plan.py、check_delivery.py）+ 模板（含 knowledge-pack.json、knowledge-rap-explainer 配方）。

8 类视频任务：产品演示、知识讲解（含 Rap/说唱）、资讯、图片成片、故事、功能动效、品牌短片、音乐视觉。知识科普的规范用法就是 README 的例句：用该技能做一期关于的概念知识科普视频，可一次性完成成片，也可只交方案或分镜。

## 边界

该技能本身不附带通用视频渲染器，也不要求固定模型或引擎；生成、渲染、配音与导出需要宿主提供相应能力。素材、模型或工具许可不从代码许可推断，须另查。59 条样片随库分发，体积大，克隆时建议稀疏克隆或只取 SKILL.md 与目录。
