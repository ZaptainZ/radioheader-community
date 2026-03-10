---
id: sw-ssh-bindinterface-vpn-local
domain: SSH, Networking, macOS
tags: BindInterface | Surge | utun | VPN | SSH 超时 | Operation timed out | 本地网络 | en0 | 路由器
refs: topics/networking-proxy.md
---
### Mac 开 VPN 后 SSH 到本地路由器超时

symptoms: `ssh user@192.168.50.1` 报 Operation timed out，但路由器确实在线
context: Mac 运行 Surge/VPN 等创建 utun 接口并劫持默认路由，SSH 流量走 VPN 隧道出不去
cause: 默认路由指向 utun（VPN 接口），本地局域网流量被错误地送入 VPN 隧道
fix: `ssh -o BindInterface=en0 user@192.168.50.1`，强制流量走物理网卡直连局域网
