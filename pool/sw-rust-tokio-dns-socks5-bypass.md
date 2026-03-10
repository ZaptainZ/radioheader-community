---
id: sw-rust-tokio-dns-socks5-bypass
domain: Rust, tokio, SOCKS5, DNS, Proxy
tags: tokio::net::lookup_host | DNS 解析 | SOCKS5 | 代理绕过 | dns_ok | local_only | 网络检测 | 连通性 | DNS 污染 | GFW | 中国大陆 | reqwest proxy | 系统 DNS | DNS 不走代理
refs: topics/networking-proxy.md
---
### tokio::net::lookup_host() 不走 SOCKS5 代理导致网络检测失败

symptoms: 应用配置了 SOCKS5 代理且 HTTP 请求正常，但网络状态检测始终返回 "local_only" 或 "offline"
context: Rust 异步应用在中国大陆通过 SOCKS5 代理访问海外 API，网络检测逻辑先 DNS 再 HTTP
fix:
1. `tokio::net::lookup_host("api.openai.com:443")` 是**系统级 DNS 调用**，不经过 SOCKS5 代理
2. 在中国大陆，被墙域名的 DNS 查询会超时或返回污染结果 → DNS 检测失败 → 提前返回 LocalOnly → HTTP HEAD（走代理的）永远不执行
3. 解决：代理启用时跳过 DNS 检查，直接走 HTTP HEAD（通过代理），以 HTTP 结果作为连通性判据
4. `RwLockReadGuard` 跨 `.await` 会阻塞写操作，需 `.clone()` 后立即释放锁
