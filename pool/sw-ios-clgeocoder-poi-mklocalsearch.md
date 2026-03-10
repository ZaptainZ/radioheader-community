---
id: sw-ios-clgeocoder-poi-mklocalsearch
domain: iOS, MapKit, Geolocation
tags: CLGeocoder | POI | MKLocalSearch | 反向地理编码 | 地址 | 商场 | 小区 | 地标 | 只有行政地址
refs: topics/ios-swiftui.md
---
### CLGeocoder 只返回行政地址，获取 POI 名称需用 MKLocalSearch

symptoms: CLGeocoder reverseGeocodeLocation 返回的地址只有省市区街道，没有附近的商场、小区等地标名
context: iOS app 需要显示用户附近的具体地点名称
cause: CLGeocoder 设计目标是行政地址解析，不提供 POI（Point of Interest）数据
fix: 用 `MKLocalSearch` 在坐标附近搜索 POI，或结合两者——CLGeocoder 获取行政地址 + MKLocalSearch 获取 POI 名称
