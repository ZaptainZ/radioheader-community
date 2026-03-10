---
id: sw-rust-json-ffi-high-freq
domain: Rust, FFI, Performance
tags: JSON FFI | 序列化开销 | 60fps | 游戏循环 | game loop | 高频调用 | 跨语言通信 | 性能瓶颈 | slow | 卡顿
refs: topics/rust-systems.md
---
### JSON FFI 在高频调用场景下开销不可接受

symptoms: 跨语言调用频繁时帧率下降、卡顿，profiler 显示序列化/反序列化占大量 CPU
context: Rust ↔ Swift/Kotlin 等跨语言通信，每帧通过 JSON 字符串传递游戏状态
cause: JSON 序列化/反序列化在 60fps（16ms/帧）循环中开销过大，挤占逻辑和渲染时间
fix: 高频路径用轻量类型直传（float/int FFI），降低调用频率，或用 shared memory / flatbuffers 替代 JSON
