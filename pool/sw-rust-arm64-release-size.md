---
id: sw-rust-arm64-release-size
domain: Rust, ARM, Embedded
tags: binary size | 二进制大小 | opt-level z | LTO | strip | panic abort | ARM64 | aarch64 | SBC | 嵌入式 | release 优化 | 1.6MB
refs: topics/rust-systems.md
---
### Rust ARM64 release 优化可产出 1.6MB 级二进制

symptoms: 需要在内存/存储受限的 ARM SBC 上运行 Rust 服务
context: Cargo.toml release profile 配置，依赖含 axum、tokio、serde、tower-http 等
cause: 默认 release 不做极致优化，二进制可能 5-10MB+
fix: 在 `[profile.release]` 中配置：
  - `opt-level = "z"`（体积优先）
  - `lto = true`（链接时优化）
  - `strip = true`（去除符号表）
  - `panic = "abort"`（去除 unwind 表）
  实测结果：含 HTTP server + WebSocket + Unix socket IPC + JSON 序列化，二进制 1.6MB，运行时 RSS ~2.9MB。ARM64 SBC 首次编译（含依赖下载）约 2m37s。
