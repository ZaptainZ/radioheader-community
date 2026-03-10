---
id: sw-net-dual-proxy-conflict
domain: Networking, Proxy
tags: 双重代理 | Surge | 路由器代理 | 冲突 | ACL | 排除 | dbus | S3 | 上传卡住 | proxy conflict
refs: topics/networking-proxy.md
---
### Mac + Surge + 路由器代理双重代理冲突及解决方式

symptoms: 网络不稳定、连接超时、S3 上传卡住
context: Mac 运行 Surge（本地代理）且连接了代理路由器

**路由器排除**: 在路由器端 ACL 排除 Mac IP。fancyss 排除必须通过 `dbus set` 持久化，手动 iptables 重启后丢失。

**S3 上传**: S3 上传前必须清除代理环境变量（`unset HTTP_PROXY HTTPS_PROXY`），否则上传请求走代理后卡住。
