---
id: sw-rust-ipc-plugin-architecture
domain: Rust, IPC, Plugin, Architecture
tags: Unix socket | IPC | 插件框架 | plugin | JSON Lines | mpsc | oneshot | 请求响应配对 | Arc shared state | 注册表 | registry | tagged enum | 热插拔
refs: topics/rust-systems.md
---
### Rust + Python 插件 IPC 架构：Arc 共享状态 + oneshot 配对

symptoms: 需要 Rust 常驻进程管理多个 Python 插件，支持双向通信和远程方法调用
context: 嵌入式/边缘设备上 Rust 守护进程 + Python 插件层，内存受限
cause: 直接用 HTTP/gRPC 太重，纯管道不支持多路复用
fix:
  - **协议**：JSON Lines over Unix socket（每行一条 `{"type":"..."}` serde tagged enum），简单高效
  - **注册表**：`HashMap<plugin_id, mpsc::Sender<String>>`，插件连接时注册，断开时自动注销
  - **请求-响应配对**：`HashMap<request_id, oneshot::Sender>`，uuid v4 生成 request_id，30s 超时自动清理
  - **共享状态**：`Arc<IpcState>` 同时传给 IPC server 和 Web server，Web 层可直接 `ipc_state.request(plugin_id, method, params)` 调用插件
  - **写协程分离**：每条连接 spawn 独立写协程（rx → socket write），避免读写交叉阻塞
  - **生命周期**：`kill_on_drop(true)` 确保主进程退出时子进程也终止，指数退避重启（5→10→20s，最多 3 次）
