---
id: sw-net-python-libressl-tls13-fail
domain: Python, SSL, macOS, Proxy
tags: LibreSSL | SSL_ERROR_SYSCALL | TLS 1.3 | Python 3.9 | Xcode python | ssl.c:1129 | 连接失败 | HTTPSConnection | chatgpt | cloudflare | 代理 SSL 错误
refs: topics/networking-proxy.md
---
### macOS Xcode 自带 Python 的 LibreSSL 无法连接需要 TLS 1.3 的站点

symptoms: Python `http.client.HTTPSConnection` 报 `SSL_ERROR_SYSCALL in connection to xxx:443` 或 `EOF occurred in violation of protocol (_ssl.c:1129)`
context: macOS 上用 `/usr/bin/python3`（Xcode 自带 3.9，LibreSSL 2.8.3）做 HTTPS 反向代理
cause: LibreSSL 2.8.3 不支持 TLS 1.3，而 Cloudflare 等 CDN 要求 TLS 1.3
fix: 用 `subprocess.Popen(["curl", "-i", "--http1.1", "--compressed", ...])` 做 relay 后端。curl 用系统 SecureTransport，支持现代 TLS。加 `--retry 2` 应对间歇性 SSL 握手失败。HTTP server 改用 `ThreadingHTTPServer` 避免并发阻塞。
