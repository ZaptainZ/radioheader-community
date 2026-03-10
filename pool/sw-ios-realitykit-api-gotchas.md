---
id: sw-ios-realitykit-api-gotchas
domain: iOS, RealityKit, 3D
tags: RealityKit | DirectionalLight | shadow | OpacityComponent | iOS 18 | 部署目标 | API 差异 | SceneKit 迁移
refs: topics/ios-swiftui.md
---
### RealityKit API 与 SceneKit 的关键差异点

symptoms: 从 SceneKit 迁移到 RealityKit 后功能缺失或编译错误

**阴影**: `DirectionalLightComponent` 没有 `.shadow` 成员（不同于 SceneKit 的 `light.castsShadow = true`）。RealityKit 的阴影由场景级别控制，非逐光源设置。

**透明度**: `OpacityComponent` 是 iOS 18.0+ 新增 API，部署目标必须 ≥ 18.0 才能使用。低版本替代方案：通过修改材质颜色的 alpha 值实现透明度变化。
