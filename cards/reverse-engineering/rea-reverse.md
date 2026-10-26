# rea-reverse（REA 逆向工作流轻量版）

- 分类: 逆向工程
- 来源: 改编
- 许可: 蒸馏自 morluto/rea 的工作流，后端工具均为开源
- 位置: ~/workspace/custom-skills/local-rea-reverse/
- 调用: 「扒一下这个 APK 的登录逻辑」
- 一句话: 反编译 → 追踪 → 带证据和局限的结论 → 复现，三条逆向线各一个技能。

## 说明

三个子技能：apk-reverse（APK 反编译定位功能）、js-reverse（JS/Electron 解包去混淆）、web-capture（网站流量抓包分析 API）。工具在 ~/workspace/tools/。

## 边界

只处理本人提供的目标；结论必须引用文件+行号；不提供绕过付费/DRM/账号系统的破解指导。Java 依赖在云电脑换机后需重装（openjdk-17）。
