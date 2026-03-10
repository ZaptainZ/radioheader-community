---
id: sw-backend-nginx-sse-send-timeout
domain: Backend, Nginx, SSE
tags: proxy_send_timeout | SSE | Server-Sent Events | 连接断开 | 消息丢失 | 60s | 超时 | proxy_buffering | 流式 | EventSource | 工具调用
refs: topics/backend-deploy.md
---
### Nginx SSE 端点需设 proxy_send_timeout

symptoms: SSE 连接在长时间无数据后静默断开，客户端收不到最终事件（如 `done`），但后端日志显示已发送
context: Nginx 反向代理 SSE 端点，后端在处理工具调用等耗时操作时 10-30 秒无数据推送
cause: `proxy_send_timeout` 默认 60s，若后端持续无数据输出超过此时间，Nginx 主动断开连接
fix: SSE location 块中设 `proxy_send_timeout 120s`（配合 `proxy_buffering off` + `proxy_read_timeout 120s` + `X-Accel-Buffering no`）；同时后端应发送心跳/状态事件保持连接活跃
