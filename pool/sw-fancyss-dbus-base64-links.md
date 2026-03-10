---
id: sw-fancyss-dbus-base64-links
domain: Networking, Proxy, Shell
tags: fancyss | dbus | ss_online_links | base64 | 订阅失败 | 明文 URL | 编码 | subscription
refs: topics/networking-proxy.md
---
### fancyss 订阅链接存 dbus 必须 base64 编码

symptoms: 订阅脚本运行但报"无法获取产品信息"或解析出乱码节点
context: 通过 `dbus set ss_online_links=` 手动设置 fancyss 订阅链接
cause: 脚本内对 `ss_online_links` 做 `base64_decode` 再提取 URL。存入明文 URL 会被 base64 解码成乱码
fix: `echo -n 'https://...' | base64 | tr -d '\n'` 得到编码值，再 `dbus set ss_online_links='编码值'`
