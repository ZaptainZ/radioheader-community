---
id: sw-rust-network-detect-three-tier
domain: Rust, Networking
tags: 网络检测 | network detection | ping | DNS | HTTP HEAD | Online | Offline | LocalOnly | 超时 | ICMP
refs: topics/rust-systems.md
---
### 网络检测三级链：ping → DNS → HTTP HEAD

context: Rust 应用需要检测网络连通性并区分 Online/LocalOnly/Offline
fix:
1. **ping 网关**（2-3s 超时）— 检测局域网连通。注意某些网关不响应 ICMP，ping 失败不代表断网
2. **DNS lookup_host**（2-3s 超时）— 检测 DNS 解析。注意代理环境下 DNS 可能被劫持
3. **HTTP HEAD 外网**（2-3s 超时）— 检测实际 Internet 连通性
- 各级结果综合判断：3 级全通 = Online，仅 ping 通 = LocalOnly，全不通 = Offline
- ping 失败后不直接判 Offline，继续做 DNS/HTTP 补救
