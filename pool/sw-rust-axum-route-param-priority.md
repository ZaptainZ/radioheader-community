---
id: sw-rust-axum-route-param-priority
domain: Rust, Axum, Web
tags: axum | 路由顺序 | route priority | :id | 参数路由 | 405 | Method Not Allowed | 路由冲突 | path parameter | 具体路由
refs: topics/rust-systems.md
---
### axum 参数路由 `/x/:id` 会吞掉同级具体路由 `/x/stats`

symptoms: `POST /api/memories/backfill` 返回 405 Method Not Allowed，allow 头显示 DELETE（因为命中了 `/api/memories/:id` 的 delete handler）
context: axum Router 同时注册 `/api/memories/:id`（delete）和 `/api/memories/backfill`（post），`:id` 路由在前
cause: axum 路由匹配时，`:id` 参数路由会匹配任意路径段，包括 `stats`、`backfill` 等字面路径。如果参数路由注册在前，具体路由永远不会被匹配到
fix: **具体路由必须注册在参数路由之前**：
  ```rust
  .route("/api/memories/stats", get(memory_stats))
  .route("/api/memories/backfill", post(memory_backfill))
  .route("/api/memories/:id", delete(delete_memory))  // 参数路由放最后
  ```
