# 如何往这个收藏集里加东西

## 加一张卡

1. 从 `templates/skill-card.md` 复制一份到 `cards/<分类slug>/` 下，文件名用技能的英文短名。
2. 必填字段：**分类、来源、一句话**。来源只许三类：自建 / 改编 / 外部。
3. 改编和外部的卡，必须写清上游链接和原许可；涉钱、涉账号抓取类的外部技能要在「边界」里标注风险。
4. 跑 `python3 scripts/build_catalog.py`，确认 CATALOG.md 已更新且脚本无报错。

## 分类 slug 对照

| slug | 分类 |
|---|---|
| writing-publishing | 写作与出版 |
| analysis-diagnosis | 分析与诊断 |
| reverse-engineering | 逆向工程 |
| video-visual | 视频与视觉 |
| behavior-decision | 行为与决策 |
| education-learning | 教育与学习 |
| external-collection | 外部收藏 |

新分类：新建 slug 目录，并在 README 的分类表里加一行。

## 不收什么

- 没有明确许可的搬运内容（只登记链接，不复制本体）。
- 需要贴出账号 cookie / 凭证才能用的操作指南——这类只在卡片「边界」里提示风险，不写步骤。
