---
id: sw-network-fakeip-bypass-breaks
domain: Networking, Proxy, OpenClash
tags: fake-ip | TUN | 断网 | 排除设备 | bypass | DNS 劫持 | 设备离线 | no internet | 路由器代理
refs: topics/networking-proxy.md
---
### fake-ip TUN 模式下排除设备会导致断网而非绕过

symptoms: 在路由器代理中"排除"某设备后，该设备完全断网而非直连
context: OpenClash / Clash fake-ip TUN 模式，想让某设备不走代理
cause: "排除"只绕过了 TUN 隧道，但 DNS 劫持仍生效——设备拿到的是 fake IP（198.18.x.x），流量却不经 TUN 解析 → 无法到达真实服务器
fix: 不用软件排除。在设备端手动设网关为主路由 IP + DNS 指向公共 DNS（如 8.8.8.8），完全不经过代理路由器

case: 家里的路由器跑 OpenClash，Mac 开着 Surge 不想双重代理，于是在 OpenClash 里把 Mac 加入排除列表。结果 Mac 直接断网。原因是 Mac 的 DNS 查询仍被路由器劫持返回 fake IP，但流量不再走 TUN 解包。最后在 Mac 网络设置里手动指定网关为光猫 IP、DNS 设成 8.8.8.8 才解决。
