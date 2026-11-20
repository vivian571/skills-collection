# guanmo-ai/guanmo-studio（观默工作室 · 产品宣传片）

- 分类: 外部收藏
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/guanmo-ai/guanmo-studio
- 调用: 未安装，收藏备查
- 一句话: 本地产品宣传片制作项目：给它一份产品配置（或产品地址），按内置模板「卡片转盘 Card Carousel」产出 15 秒 1920×1080 60fps 横版短片，另可导出六段分轨剪辑素材。

## 说明

2026-11-19 验真：GitHub API 与仓库原文实查，★63、fork 15，MIT，仓库建于 2026-11-18（昨日新建），pushed 2026-11-19，版本 0.1.0，README 自称「0.1 预览阶段」。树内有 SKILL.md（templates/card-carousel/SKILL.md，5,659 字节）：输入 config.json（品牌名/一句话介绍、7–31 张卡片、6 张精选卡、1 张主角卡、背景预设、配乐音效），或把 prompt.md＋产品地址交给编码 Agent 按模板改配置出片。工具链：Three.js 场景＋Playwright/Chromium 逐帧渲染＋FFmpeg 编码＋Python Pillow；配乐音效本地合成（原创 BGM＋CC0 音效）。不调用付费模型、不需要登录与密钥；依赖 npm 三包（esbuild、playwright、three）＋Pillow，系统需 Node 22+、Python 3.10+、FFmpeg。发现渠道：Vivian 2026-11-19 发来推帖截图点名核实。

## 边界

仅收藏登记，未安装未实测。已做静态安全审查（2026-11-19，scripts/ 全部 28 个 Node 脚本与模板 Python 脚本）：运行期无对外请求（唯一 fetch 读本地配置，预览服务器只绑 127.0.0.1），子进程只调 node/docker/ffmpeg/python，不读 API key/token 与 .ssh/.aws，文件读写限仓库内目录，未见可疑行为；此为静态结论，未实际运行验证。成熟度风险大于安全风险：目前只有一个模板、只支持 15 秒横版，竖版与其它时长官方明说未实现；与 Vivian 日常管线（9:16 AI 新闻、手绘讲解）形态不合，潜在用途是给 Jev 做横版产品宣传片时小试。在线体验页：guanmo-ai.github.io/guanmo-studio。
