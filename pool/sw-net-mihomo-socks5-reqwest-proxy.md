---
id: sw-net-mihomo-socks5-reqwest-proxy
domain: Rust, reqwest, Proxy, mihomo, Clash
tags: mihomo | Clash Meta | SOCKS5 | reqwest socks | proxy-provider | 订阅链接 | 代理 | 翻墙 | 机场 | ARM64 | 低内存 | proxy config.yaml | External Controller | url-test | DOMAIN-SUFFIX | DIRECT
refs: topics/networking-proxy.md
---
### 用 mihomo + reqwest SOCKS5 为 Rust 应用添加透明代理出网

symptoms: ARM 设备无法直连海外 API（openai.com/chatgpt.com/anthropic.com），需要代理但不想全局翻墙
context: 4GB ARM SBC 上运行 Rust 服务，需按域名选择性代理 AI API 请求
fix:
1. mihomo 二进制 ~12MB，ARM64 空闲 ~30-50MB 内存，适合低功耗设备
2. Cargo.toml: `reqwest = { version = "0.12", features = ["json", "stream", "socks"] }`
3. 代码构造代理客户端: `reqwest::Proxy::all("socks5://127.0.0.1:7891")` → `Client::builder().proxy(proxy).build()`
4. mihomo config.yaml 关键段: `proxy-providers` 填机场订阅 URL + interval 自动更新; `proxy-groups` 用 `url-test` 自动选节点; `rules` 用 `DOMAIN-SUFFIX,openai.com,PROXY` 按域名代理，`MATCH,DIRECT` 其余直连
5. External Controller API (`127.0.0.1:9090`): `GET /proxies` 列节点, `PUT /proxies/{group}` 切节点
