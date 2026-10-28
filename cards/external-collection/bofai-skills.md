# BofAI/skills（Bank of AI 技能集，含 x402-payment）

- 分类: 外部收藏
- 来源: 外部（其中 x402-payment 已安装本地）
- 许可: MIT
- 位置: https://github.com/BofAI/skills（x402-payment 本地安装：~/workspace/custom-skills/local-x402-payment/）
- 调用: 未启用付款通道，收藏备查
- 一句话: Bank of AI 的技能合集仓（TRON 生态为主）；其中的 x402-payment 技能让 agent 用 USDT/USDD/USDC 经 x402 协议为付费 API 付款（带 --dry-run 与单笔上限）。

## 说明

2026-10-22 Vivian 点名安装其中 x402-payment（原话指令 `npx skills add https://github.com/BofAI/skills --skill x402-payment`）。验真（2026-10-28，GitHub API 一手）：★163，MIT，默认分支 develop，最近 pushed 2026-10-27；默认分支树内 6 个 SKILL.md（sunperp / sunpump-agent / sunswap / tronscan / usdd / wallet-cli）。注意：x402-payment 不在默认分支——2026-10-22 安装时默认分支没有这个技能，是从未合并的 feature 分支 feat/x402-payment-1.0.1-gasfree 装的，装的版本与主线状态要分开看。

## 边界

仅收藏登记本仓；x402-payment 本地虽已装，但付款 CLI 安装与钱包注资都未做——涉及真实资金，须 Vivian 明确拍板才动，目前该技能付不出任何钱。
