# wechat-draft-publisher（公众号草稿箱发布）

- 分类: 写作与出版
- 来源: 自建
- 许可: 自有（源仓库 vivian571/wechat-publisher）
- 位置: ~/workspace/custom-skills/local-wechat-draft-publisher/
- 调用: 「把这篇推到公众号草稿箱」
- 一句话: Markdown → 公众号样式 HTML → 经官方 API 进草稿箱，到此为止，发表永远手动。

## 说明

单次运行（无守护进程），带出口 IP 变化检查。md→HTML 与封面图处理已实测通过。

## 边界

只调 `draft/add`，绝不代点发表。API 上传未做真机实测：需要本人填 AppID/AppSecret 并配出口 IP 白名单；云电脑出口 IP 会变，白名单可能不稳，备选走固定 IP 机器。
