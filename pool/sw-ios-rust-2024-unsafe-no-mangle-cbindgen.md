---
id: sw-ios-rust-2024-unsafe-no-mangle-cbindgen
domain: iOS, Rust, FFI
tags: Rust 2024 | no_mangle | unsafe | cbindgen | C header | FFI | 编译错误 | bridging header
refs: topics/ios-swiftui.md
---
### Rust 2024 edition 的 #[unsafe(no_mangle)] 与 cbindgen 不兼容

symptoms: Rust 2024 edition 项目中 cbindgen 生成的 C header 缺少函数声明或报解析错误
context: Rust 2024 edition 要求 `#[unsafe(no_mangle)]` 替代 `#[no_mangle]`，但 cbindgen 0.27 不识别新语法
cause: cbindgen 解析 AST 时不理解 `unsafe(no_mangle)` 属性，跳过了这些函数
fix: 手写 C header 文件声明 FFI 函数，不依赖 cbindgen 自动生成。注意 iOS 项目中若有双份 header（如 core/ 和 ios/Bridge/），必须手动保持同步
