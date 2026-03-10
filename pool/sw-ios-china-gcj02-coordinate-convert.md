---
id: sw-ios-china-gcj02-coordinate-convert
domain: iOS, MapKit, China
tags: GCJ-02 | WGS-84 | 坐标偏移 | 中国 | coordinate | 地图偏移 | 位置不准 | MKLocalSearch | 火星坐标
refs: topics/ios-swiftui.md
---
### 中国境内 MKLocalSearch 坐标需 WGS-84 → GCJ-02 转换

symptoms: 地图上标注点或搜索结果位置偏移数百米
context: 在中国大陆使用 Apple Maps / MKLocalSearch，GPS 原始坐标（WGS-84）与地图显示不一致
cause: 中国法律要求地图使用 GCJ-02 坐标系（"火星坐标"），GPS 原始 WGS-84 坐标在中国地图上会产生偏移
fix: 在中国境内使用前将 WGS-84 坐标转换为 GCJ-02。注意 Apple Maps 在中国自动使用 GCJ-02，但 CLLocationManager 返回的是 WGS-84
