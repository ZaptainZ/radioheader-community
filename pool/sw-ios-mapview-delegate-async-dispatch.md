---
id: sw-ios-mapview-delegate-async-dispatch
domain: iOS, MapKit, Threading
tags: MKMapView | delegate | 闪退 | crash | preferredConfiguration | annotation | 聚合 | clustering | async dispatch | 竞态 | race condition
refs: topics/ios-swiftui.md
---
### MKMapView delegate 回调中禁止同步修改配置和 annotation

symptoms: MKMapView 随机闪退，崩溃堆栈指向聚合视图或配置切换

**配置切换**: 在 delegate 回调（如 `mapView(_:viewFor:)`）中同步修改 `preferredConfiguration` 会导致内部状态冲突闪退——MKMapView 正在创建聚合视图时不允许切换配置。fix: `DispatchQueue.main.async { mapView.preferredConfiguration = ... }`

**annotation 操作**: 在 `regionDidChangeAnimated` 等 delegate 回调中同步调用 `removeAnnotations`/`addAnnotations` 可能与聚合引擎竞态。fix: 用 `DispatchQueue.main.async` 延迟到下一个 run loop + 设最小操作间隔做 coalescing
