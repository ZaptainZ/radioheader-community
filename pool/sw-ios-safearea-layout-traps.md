---
id: sw-ios-safearea-layout-traps
domain: iOS, SwiftUI, Layout
tags: ignoresSafeArea | 安全区 | safe area | PageTabViewStyle | 全屏 | fullscreen | frame | maxWidth | .infinity | NavigationStack | toolbar hidden | iPad 兼容
refs: topics/ios-swiftui.md
---
### SwiftUI 安全区与布局常见陷阱汇总

symptoms: 全屏视图仍有安全区内缩、`.frame(width: .infinity)` 不生效、iPad 兼容模式布局异常

**PageTabViewStyle 安全区**: `.ignoresSafeArea()` 只扩展 TabView frame，不移除 page 内容的安全区内缩。fix: 用 GeometryReader 获取全屏尺寸，显式 `.frame(width:height:)` 设置 page 大小。

**全屏视图三件套**: NavigationStack 内的全屏视图需同时设置 `.ignoresSafeArea()` + `.navigationBarBackButtonHidden(true)` + `.toolbar(.hidden, for: .navigationBar)`，缺一会有残留空间。

**frame 写法**: `.frame(width: .infinity)` 无效（设置了精确宽度为 infinity），必须用 `.frame(maxWidth: .infinity)`。

**iPad 兼容模式**: `TARGETED_DEVICE_FAMILY=1` 时 `bottomSafeArea=0`，依赖百分比 offset 的公式需设最小可见高度保底，避免除零或内容不可见。
