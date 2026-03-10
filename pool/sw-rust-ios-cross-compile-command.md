---
id: sw-rust-ios-cross-compile-command
domain: Rust, iOS, Cross-compilation
tags: Rust | iOS | 交叉编译 | aarch64-apple-ios | cargo build | target | cargo env
refs: topics/rust-systems.md
---
### Rust iOS 交叉编译命令与环境

context: 在 macOS 上编译 Rust 库供 iOS 项目链接
fix: `source ~/.cargo/env && cargo build --target aarch64-apple-ios`。确保 Cargo.toml crate-type 只含 `["staticlib", "lib"]`（不能有 cdylib）
