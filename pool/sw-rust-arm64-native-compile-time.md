---
id: sw-rust-arm64-native-compile-time
domain: Rust, ARM, Build
tags: ARM64 | SBC | 原生编译 | compile time | axum | tokio | serde | 2m37s | 兼容性
refs: topics/rust-systems.md
---
### ARM64 SBC 原生编译 Rust 首次约 2m37s，无兼容性问题

symptoms: 担心 ARM64 SBC 上 Rust 编译太慢或有兼容问题
context: 在 4GB ARM64 SBC 上直接编译 Rust 项目（含 axum/tokio/serde 等依赖）
fix: 首次完整编译约 2m37s，增量编译更快。无兼容性问题，release 优化（opt-level="z" + LTO + strip + panic="abort"）产出 1.6MB 二进制，RSS ~2.9MB
