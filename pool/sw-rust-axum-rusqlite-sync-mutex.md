---
id: sw-rust-axum-rusqlite-sync-mutex
domain: Rust, axum, SQLite
tags: rusqlite | Connection | Sync | Send | Mutex | axum | Handler | AppState | trait bound | 编译错误 | not satisfied | Arc | 状态共享 | shared state
refs: topics/rust-systems.md
---
### rusqlite::Connection 非 Sync，axum 共享 SQLite 需 Mutex 包装

symptoms: axum 路由全部编译失败，报 `the trait bound Handler<_, _> is not satisfied`，错误指向每个路由的 handler 函数
context: 在 axum AppState 中放入包含 `rusqlite::Connection` 的结构体（通过 `Arc` 共享），注册路由时编译失败
cause: `rusqlite::Connection` 实现了 `Send` 但不是 `Sync`。axum 的 `Handler` trait 要求 AppState 为 `Clone + Send + Sync + 'static`，`Arc<T>` 只有当 `T: Send + Sync` 时才是 `Sync`
fix: 将 Connection 包装为 `Mutex<Connection>`（`std::sync::Mutex` 即可），结构体自动满足 `Send + Sync`。各方法内 `self.conn.lock().unwrap()` 获取连接。无需 `tokio::Mutex`——SQLite 操作本身是同步的且很快

#### case
一个 Web 服务的包管理模块用 SQLite 追踪已安装包和源配置。直接持有 `Connection` 时，新增任何路由都导致全部 Handler 编译失败（错误信息巨长但核心是 trait bound）。改为 `Mutex<Connection>` 后一次编译通过，无性能影响。
