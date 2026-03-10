---
id: sw-ios-task-inherits-mainactor
domain: iOS, SwiftUI, Concurrency
tags: 白屏 | 启动慢 | 首次加载 | white screen | slow launch | 10s+ | hang | Main Actor | Task | Task.detached
refs: topics/ios-swiftui.md
---
### Task {} 在 @MainActor 上下文中继承主线程，I/O 阻塞导致白屏

symptoms: 应用启动后 10s+ 白屏，首次加载卡死
context: SwiftUI `.onAppear` 或 `body` 中用 `Task {}` 发起 I/O 操作（iCloud、网络、磁盘）
cause: `Task {}` 继承调用者的 Actor 隔离；在 @MainActor 上下文中创建 = 仍在主线程执行，I/O 阻塞 UI
fix: 改用 `Task.detached(priority: .userInitiated) { ... }` 脱离主线程
verified: 启动白屏从 10s+ → <1s

case: 一个写日记的 app，启动时在 `.onAppear` 里用 `Task {}` 加载 iCloud 中的日记列表。用户每次打开 app 都要盯着白屏等 10 秒以上。改成 `Task.detached` 后首屏秒开，iCloud 数据在后台加载完成后自动刷新列表。
