---
id: sw-ios-realitykit-scenekit-migration
domain: iOS, RealityKit, SceneKit, 3D
tags: SceneKit 迁移 | RealityKit | SCNAction | entity.move | 动画链 | animation chain | completion callback | asyncAfter | PerspectiveCamera | 镜头 | camera orbit | look-at | RealityView | virtual camera | UnlitMaterial | emission | 材质闪烁 | flash effect | OpacityComponent | iOS 18
refs: topics/ios-swiftui.md
---
### SceneKit → RealityKit 迁移：动画链、镜头、材质效果的 API 对应

symptoms: SceneKit 进入维护模式，需迁移到 RealityKit；SCNAction completion 链式回调在 RealityKit 中无直接对应
context: 程序化几何体场景（无 .scn/.usdz 资源），包含镜头轨道旋转、角色动画、投射物飞行、材质闪烁等效果

**动画链**: SCNAction.sequence + completion block → `entity.move(to:relativeTo:duration:timingFunction:)` + `DispatchQueue.main.asyncAfter`。已知时长用 asyncAfter 比订阅 `AnimationEvents.PlaybackCompleted` 更简单可靠。

**镜头轨道**: SCNCamera + SCNLookAtConstraint → PerspectiveCamera 作为 orbitEntity 子节点 + `look(at:from:relativeTo:)` 设一次朝向。orbit Y 轴旋转自动维持 look-at 目标（父子变换组合），不需要约束。

**视图层**: SCNView + UIViewRepresentable (~25行) → `RealityView { content in }` + `content.camera = .virtual` (~14行，iOS 18+ SwiftUI 原生)。

**材质闪烁**: SCNMaterial.emission → 无直接对应。用 swap `entity.model.materials` 到 `UnlitMaterial(color: .white)` 再换回。

**透明度**: SCNNode.opacity → `OpacityComponent(opacity:)` (iOS 18+ 新增)。SCNAction.fadeOut → 直接设 `OpacityComponent(opacity: 0)`。

**注意**: `DirectionalLightComponent` 没有 `.shadow` 属性（不同于 SCNLight.castsShadow）。
