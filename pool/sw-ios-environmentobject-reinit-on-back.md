---
id: sw-ios-environmentobject-reinit-on-back
domain: iOS, SwiftUI, Navigation
tags: EnvironmentObject | 状态丢失 | 导航返回 | 列表重置 | state lost | back navigation | reinit | ViewModel
refs: topics/ios-swiftui.md
---
### 导航返回后 @EnvironmentObject 可能被重新初始化导致状态丢失

symptoms: 从详情页返回列表页后，列表滚动位置、筛选状态等被重置
context: SwiftUI NavigationStack 中使用 @EnvironmentObject 管理列表状态
cause: SwiftUI 在导航跳转时可能重建视图层级，导致 @EnvironmentObject 注入的对象被重新初始化
fix: 用独立的 ViewModel（@StateObject 或外部持有）持久化状态，不依赖 @EnvironmentObject 的生命周期
