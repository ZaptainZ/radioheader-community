---
id: sw-ios-asyncimage-retry-id
domain: iOS, SwiftUI, Networking
tags: AsyncImage | 重试 | retry | 图片加载失败 | image reload | 刷新 | .id()
refs: topics/ios-swiftui.md
---
### AsyncImage 失败重试用 .id(UUID()) 强制重建

symptoms: AsyncImage 加载失败后不会自动重试，用户看到占位图无法恢复
context: SwiftUI AsyncImage 加载网络图片
cause: AsyncImage 不提供内置重试机制，失败后 SwiftUI 认为视图状态未变不会重新请求
fix: 重试时给 AsyncImage 设 `.id(UUID())`，强制 SwiftUI 销毁并重建实例从而触发新请求
