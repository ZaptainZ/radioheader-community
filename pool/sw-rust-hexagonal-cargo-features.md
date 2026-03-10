---
id: sw-rust-hexagonal-cargo-features
domain: Rust, Architecture
tags: 六边形架构 | Hexagonal | Ports & Adapters | Cargo features | 跨平台 | 模块化 | 游戏架构
refs: topics/rust-systems.md
---
### 六边形架构 + Cargo features 实现跨平台模块化

context: 跨平台游戏或应用的 Rust 架构设计
fix:
- 六边形架构（Ports & Adapters）：Rust Core 定义接口（ports），各平台实现适配器（adapters/shells）
- 适合跨平台场景：iOS/Android/Web 共享 Core，各平台只实现渲染/输入/音频适配器
- Cargo features 按需启用功能模块（network/audio/physics），保持编译产物精简
