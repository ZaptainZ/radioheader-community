---
id: sw-rust-axum-route-param-syntax
domain: Rust, Axum, Web
tags: axum | 路由参数 | route parameter | path param | 405 | Method Not Allowed | fallback | :id | {id} | 0.7 | 0.8
refs: topics/rust-systems.md
---
### axum 0.7.x 路由参数用 `:id`，`{id}` 是 0.8+ 语法

symptoms: POST/PUT 请求返回 405 Method Not Allowed，allow 头只有 GET/HEAD（说明请求落入了 ServeDir fallback 而非目标路由）
context: axum 0.7.x，路由含路径参数如 `/api/plugins/{id}/call`
cause: axum 0.7.x 使用 `:id` 语法（如 `/api/plugins/:id/call`），`{id}` 是 0.8+ 引入的新语法。用错语法时路由不匹配，请求被 fallback 处理
fix: 将 `{id}` 改为 `:id`。axum 版本升级到 0.8+ 后再切换为 `{id}` 语法
