# eternityspring/shuohao-skills（AI 短剧制作技能集）

- 分类: 外部收藏
- 来源: 外部
- 许可: Apache-2.0
- 位置: https://github.com/eternityspring/shuohao-skills
- 调用: 未安装，收藏备查
- 一句话: AI 短剧制作的 7 个技能：小说改编大纲、角色设定、角色参考图、场景道具设定、剧本、分镜场位、分镜，一路做到可投产的分镜包。

## 说明

2026-10-27 验真：GitHub 实查公开仓，★5,427，fork 751，Apache-2.0，创建于 2026-08-06，121 个提交，默认分支 main。7 个技能：novel-outline（五件套改编大纲，14 道脚本质检关）、novel-characters（角色设定集）、character-refs（真正生成角色参考图，锚定一张正面全身图再出各角度）、novel-art（场景与道具设定集，10 道质检关）、novel-script（剧本，按阅读速度估算单集时长，首 3 节拍设冷开场钩子，10 道质检关）、novel-staging（开场站位俯视图，可拖拽后导出）、novel-storyboard（分镜，片段≤15 秒、切镜 2–5 秒硬关，18 道质检关，附 MiniMax H3 / Seedance 投产包）。报告默认中文界面，可加 --lang en 出英文报告。运行要求 Node ≥18，脚本只用标准库，无 npm 依赖；支持 Claude Code 与 Codex，但本身不绑定运行时，任何能读 SKILL.md 并跑 Node 脚本的 agent 都可用。另有 scripts/report.mjs 可把 5 个阶段报告拼成一页。发现渠道：Vivian 2026-10-27 微信发来的链接。功能域：短剧 / 视频制作 / 剧本与分镜。

## 边界

仅收藏登记，未安装未实测。出图出视频要走作者自己的 ComfyUI / 模型配额（Qwen Image、GPT Image 2 等），取用前先确认各技能的模型与配额要求。
