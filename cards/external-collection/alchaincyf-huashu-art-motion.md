# alchaincyf/huashu-art-motion（花叔艺术动画）

- 分类: 外部收藏
- 来源: 外部（已安装本地）
- 许可: MIT
- 位置: https://github.com/alchaincyf/huashu-art-motion（本地安装：~/workspace/custom-skills/local-huashu-art-motion/）
- 调用: 「用 huashu 做一条 XX 艺术动画」
- 一句话: 代码绘制的艺术动画技能：35+ 种艺术风格 + 9 种解说语法，流程为镜头表（锁画风/色板/角色）→ storyboard_lint → 逐镜渲染 → 拼接混口播 → qa → deliver 门禁出片。

## 说明

2026-10-27 Vivian 本人发送，问功能与「是否可以安排」，随后点选安装。验真（2026-10-28，GitHub API 一手）：★5,595，MIT，根目录有 SKILL.md，最近 pushed 2026-10-16。已装本地（v1.2.0，本体未改）并冒烟测通过（t3 财经图表语法 + paper 色板 7 秒片段，lint 黄灯无红灯、qa 通过、deliver 门禁跑通）；2026-10-28 又以它为抖音 #vibe知识大赏 姆潘巴正片做了 15 秒先导小样实测。注意别与同作者的 alchaincyf/huashu-design（设计技能，已另行收录）混淆，是两个仓库。

## 边界

运行须钉 playwright==1.49.1（对应本机缓存 chromium-1148；最新版 chromium 下载在本机网络会超时）。硬规则：一片一画风、拒绝翻页 PPT 运镜、蓝紫渐变默认禁用（要用须 --allow-blue-purple 写理由）。多镜拼接与口播混音已在小样实测，scenes 手工代码镜头未验。
