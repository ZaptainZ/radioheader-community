---
id: sw-net-fancyss-vs-shellcrash
domain: Networking, Router, Proxy
tags: fancyss | ShellCrash | Merlin | 路由器代理 | en0 | interface-name | 代理失效 | 方案对比
refs: topics/networking-proxy.md
---
### Merlin 路由器代理方案：fancyss 最稳定，ShellCrash 有硬编码陷阱

symptoms: ShellCrash 安装后代理完全不工作
context: Merlin 路由器选择代理方案
cause: ShellCrash `start.sh` 硬编码 `interface-name: en0`（Mac 网卡名），路由器上无此接口导致代理完全失效
fix: Merlin 路由器推荐用 fancyss，稳定且社区支持好。V2ray 订阅链接加 `?sub=3` 参数返回标准 base64 vmess 格式兼容 fancyss；ShellCrash clash 格式订阅需第三方转换服务
