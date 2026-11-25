# danielwh2/sprite-stacking（四视图像素画转可旋转伪 3D 精灵）

- 分类: 外部收藏
- 来源: 外部
- 许可: MIT
- 位置: https://github.com/danielwh2/sprite-stacking
- 调用: 未安装，收藏备查
- 一句话: 把四张正交像素视图（顶/侧/正/背）雕成体素再切层，做成可旋转的伪 3D 精灵：附切片 CLI 与可拖拽转盘查看器，单技能。

## 说明

2026-11-25 日采验真：GitHub API 实查 ★782，许可 MIT，最近 pushed 2026-11-24，默认分支 main。仓库树含 1 个 SKILL.md（skills/sprite-stacking/SKILL.md），另附 views_to_slices.py 切片 CLI 与 viewer.html 转盘查看器。发现渠道：网页搜索新发现（skilld.dev 2026-11-18–25 本周趋势榜第 6 项，X @dwhitedesign 原帖，归属经搜索确认为 danielwh2/sprite-stacking）。功能域：像素画 / 游戏美术 / 精灵动画。流程：四视图 → 体素雕刻（仅保留四视图都覆盖的部分）→ 按层切片 → 逐层旋转压扁抬升渲染；支持 15–20 层粗颗粒与 32–48 层精细两种规格，可导出 16 方向 PNG；需 Python 3 + Pillow/NumPy。作者自述 sprite stacking 是老技术，本技能只加了雕刻步骤与 agent 工作流。

## 边界

仅收藏登记，未安装未实测；技能自带规则：没渲染看过就不出货，按参考登记。
