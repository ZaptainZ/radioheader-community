---
id: sw-ios-swift6-deinit-nonisolated
domain: iOS, Swift, Concurrency
tags: Swift 6 | deinit | nonisolated | MainActor | Sendable | CADisplayLink | 编译错误 | actor isolation | 并发检查
refs: topics/ios-swiftui.md
---
### Swift 6 中 @MainActor 类的 deinit 是 nonisolated，访问非 Sendable 属性需特殊处理

symptoms: Swift 6 严格并发检查下，@MainActor 类的 deinit 中访问属性报编译错误
context: Swift 6 + @MainActor 类 + deinit 中需要清理非 Sendable 资源（如 CADisplayLink）
cause: Swift 6 规定 deinit 始终是 nonisolated，无法继承类的 @MainActor 隔离；CADisplayLink 等 UIKit 类型不是 Sendable
fix: 在 deinit 中访问非 Sendable 属性时标记 `nonisolated(unsafe)`，或将清理逻辑移到 deinit 之前显式调用
