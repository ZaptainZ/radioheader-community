---
id: sw-ios-nested-navigationstack-ipad
domain: iOS, SwiftUI, Navigation
tags: NavigationStack | 嵌套 | iPad | navigationDestination | 导航失效 | 点击无反应 | nested | navigation broken
refs: topics/ios-swiftui.md
---
### 嵌套 NavigationStack 导致 iPad 上 navigationDestination 失效

symptoms: iPad 上点击导航链接无反应，navigationDestination 不触发；iPhone 上可能正常
context: View 内部嵌套了 `NavigationStack{}`，外层已有另一个 NavigationStack
cause: SwiftUI 不支持多层 NavigationStack 嵌套，内层会劫持导航上下文，iPad 上表现为完全失效
fix: 移除内层 NavigationStack，确保整个导航树只有一个顶层 NavigationStack
