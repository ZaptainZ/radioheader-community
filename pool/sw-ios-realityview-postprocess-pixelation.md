---
id: sw-ios-realityview-postprocess-pixelation
domain: iOS, RealityKit, SwiftUI, Metal
tags: layerEffect | RealityView | 禁止符号 | prohibition symbol | stitchable | PostProcessEffect | customPostProcessing | 像素化 | pixelation | pixellate | CAMetalLayer | drawableSize | magnificationFilter | nearest | 后处理 | post-processing | iOS 26 | 崩溃 | crash | final class | struct | 延迟初始化 | Unable to render flattened | PlatformViewRepresentableAdaptor
refs: topics/ios-swiftui.md
---
### RealityView 像素化后处理：layerEffect 不可用、PostProcessEffect 崩溃的正确做法

symptoms: RealityView 上加 `.layerEffect()` 显示黄底红色禁止符号；PostProcessEffect 用 struct 或在 make/立即 update 中设置导致崩溃

**`.layerEffect()` 对 RealityView 无效**: RealityView 通过独立 CAMetalLayer 渲染，SwiftUI 无法光栅化其输出（日志: `Unable to render flattened version of PlatformViewRepresentableAdaptor`）。这是架构限制，非代码错误，`.drawingGroup()` 也无法修复。

**PostProcessEffect (iOS 26+) 正确做法**:
1. 必须用 `final class`（非 struct）：`final class MyEffect: PostProcessEffect, @unchecked Sendable`
2. 必须延迟设置：在 `.task { try? await Task.sleep(for: .milliseconds(500)) }` 后设 `@State` flag，`update` 闭包检测 flag 后设 `content.renderingEffects.customPostProcessing = .effect(myEffect)`
3. 在 `make` 闭包或立即 `update` 中设置会在 `prepare(for:)` 之前崩溃（无堆栈，RealityKit 内部错误）

**CAMetalLayer 降级方案 (iOS 18~25)**: 用 UIViewRepresentable 探针视图 + CADisplayLink，递归搜索 window UIView 层级找到 RealityView 的 CAMetalLayer，设 `magnificationFilter = .nearest` + 缩小 `drawableSize`。需每帧重新应用（RealityKit 可能重置 drawableSize）。
