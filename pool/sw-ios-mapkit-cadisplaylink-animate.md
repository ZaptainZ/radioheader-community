---
id: sw-ios-mapkit-cadisplaylink-animate
domain: iOS, MapKit, Animation
tags: MKMapView | 动画 | animation | camera | UIView.animate | CADisplayLink | 逐帧 | mapViewDidChangeVisibleRegion | regionDidChangeAnimated
refs: topics/ios-swiftui.md
---
### UIView.animate 无法驱动 MKMapView camera，需用 CADisplayLink 逐帧插值

symptoms: 用 UIView.animate 设置 MKMapView camera 无动画效果，直接跳到终点
context: 需要对 MKMapView 做自定义 camera 动画（飞行、平移等）
cause: MKMapView 的 camera 属性不参与 UIView 动画系统（不是 animatable property）
fix: 用 CADisplayLink 逐帧插值 camera 参数（center、distance、heading），手动实现动画曲线

**delegate 回调区别**: `mapViewDidChangeVisibleRegion` 在动画进行中每帧触发（适合实时响应），`regionDidChangeAnimated` 仅在动画结束时触发一次（适合最终结果处理）
