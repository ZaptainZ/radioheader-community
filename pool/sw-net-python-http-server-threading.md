---
id: sw-net-python-http-server-threading
domain: Python, Networking, HTTP
tags: HTTPServer | 单线程 | blocking | ThreadingHTTPServer | 并发 | concurrent | 请求阻塞
refs: topics/networking-proxy.md
---
### Python http.server.HTTPServer 是单线程的，并发请求会阻塞

symptoms: HTTP 服务器处理一个请求时其他请求完全卡住，串行执行
context: 用 Python 内置 `http.server` 做简单 HTTP 服务
cause: `HTTPServer` 默认单线程同步处理，一次只能服务一个请求
fix: 替换为 `ThreadingHTTPServer`（Python 3.7+），每个请求在独立线程中处理
