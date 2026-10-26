# edulab（教育技能集合）

- 分类: 教育与学习
- 来源: 外部
- 许可: Apache-2.0
- 位置: ~/workspace/custom-skills/local-edulab/（上游 https://github.com/wy51ai/edulab）
- 调用: 「解这道立体几何题」「随机出一道圆锥曲线题」「把这道物理题做成讲解视频」
- 一句话: 把学科问题转成可交互的教学网页和带配音的讲解视频，6 个子技能。

## 说明

2026-10-20 应要求安装并冒烟通过（上游 ★1,573）。子技能：
- edu-solid-geometry：立体几何（线面角、二面角、点到面距离、体积）→ 交互教学网页，建系+向量法
- edu-analytic-geometry：解析几何/圆锥曲线 → 交互教学网页
- edu-chem-reaction：化学反应 → 交互教学网页
- edu-chem-video / edu-math-video / edu-physics-video：化学/数学/物理讲解视频

三入口：文字题目、上传图片识题、随机出题。计算核心依赖 sympy（本机已有 1.12）；立体几何 kernel 自检全过，generate.py 实测生成出完整的自包含 HTML 教学页。

## 边界

题型偏高中学段（立体几何、圆锥曲线）。图片识题走视觉读图，生成结果先回显确认再求解；随机题答案不规整会自动重抽。仓库 42MB 主要是演示图，技能本体不大。
