# agent-trace（Agent 轨迹分析三件套）

- 分类: 分析与诊断
- 来源: 改编
- 许可: 思路源自 xuanyuanzhifeng/dsh-plugin-agent-workflow（MIT），代码独立重写
- 位置: ~/workspace/custom-skills/local-agent-trace/
- 调用: 「看一下这次 agent 跑了什么」「这次调用为什么这么贵」
- 一句话: 把 Agent 的 JSONL 轨迹投影成执行链，并重建每次请求的上下文做 token 尸检。

## 说明

三个子技能：trace-inspector（轨迹检查器，轮次→请求→响应→工具链）、context-autopsy（上下文尸检，重建 messages 并找膨胀点）、tool-forensics（工具调用链，耗时/失败/重试带证据）。纯 Python 标准库，已在合成轨迹上测过。

## 边界

真实 agent 日志的适配器尚未在真实日志上实测。与 rea-reverse 互补：这个看动态轨迹，那个做静态逆向。
