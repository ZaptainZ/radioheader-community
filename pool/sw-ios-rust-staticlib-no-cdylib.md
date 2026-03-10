---
id: sw-ios-rust-staticlib-no-cdylib
domain: iOS, Rust, FFI
tags: Rust | iOS | cdylib | staticlib | dyld | SIGABRT | 崩溃 | crash | Cargo.toml | crate-type | DerivedData | .dylib
refs: topics/ios-swiftui.md
---
### Rust iOS 项目 crate-type 含 cdylib 导致 dyld SIGABRT 崩溃

symptoms: iOS app 启动时 dyld 报错 SIGABRT，指向 Rust 编译产物
context: Rust 库通过 staticlib 链接到 iOS 项目，Cargo.toml crate-type 中同时包含 cdylib
cause: cdylib 生成的 .dylib 与 iOS 的静态链接机制冲突，dyld 尝试加载动态库失败
fix: Cargo.toml 中 crate-type 只保留 `["staticlib", "lib"]`，删除 `"cdylib"`。删除后还需清理残留 .dylib 文件 + Xcode DerivedData
