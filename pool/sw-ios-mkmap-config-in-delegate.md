---
id: sw-ios-mkmap-config-in-delegate
domain: iOS, MapKit, MKMapView
tags: MKMapView | preferredConfiguration | 闪退 | crash | 聚合 | cluster | MKClusterAnnotation | 缩放 | pinch zoom | delegate 回调 | 竞态 | race condition | configuration switch | HybridFlyover | Standard
refs: topics/ios-swiftui.md
---
### MKMapView delegate 回调中禁止同步修改 preferredConfiguration

symptoms: 双指缩放时闪退，日志显示聚合视图创建后紧跟配置切换
context: 在 `mapViewDidChangeVisibleRegion` 或 `regionDidChangeAnimated` 中根据 camera distance 同步切换 `preferredConfiguration`（如 Standard ↔ HybridFlyover）
cause: MKMapView 正在创建 MKClusterAnnotation 视图时，同步修改 `preferredConfiguration` 导致内部状态冲突
fix: 将 `preferredConfiguration` 赋值包装在 `DispatchQueue.main.async` 中延迟到下一个 run loop。用 DispatchWorkItem + cancel 做 coalescing，快速来回缩放只执行最后一次切换

---
### MKMapView annotation 增删也需异步 + coalescing

symptoms: 快速缩放时偶发闪退，日志显示 annotation 增删与聚合视图创建交替出现
context: 在 delegate 回调链中触发 `removeAnnotations`/`addAnnotations`，与 MKMapView 内部聚合计算在同一 run loop
cause: annotation 变更触发聚合重算，下一次变更在聚合完成前进入，内部状态不一致
fix: annotation 操作通过 coordinator 统一管理，`DispatchQueue.main.async` 延迟执行 + DispatchWorkItem coalescing（只执行最后一次）+ 两次操作间强制最小间隔 200ms
