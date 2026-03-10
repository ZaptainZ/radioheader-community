---
id: sw-ios-mklocalsearch-ios17-natural-language
domain: iOS, MapKit, Search
tags: MKLocalSearch | iOS 17 | naturalLanguageQuery | 搜索无结果 | empty results | 空数组 | POI
refs: topics/ios-swiftui.md
---
### MKLocalSearch 在 iOS 17 上必须设 naturalLanguageQuery 否则返回空结果

symptoms: MKLocalSearch 返回空数组，无错误信息
context: iOS 17+ 环境下使用 MKLocalSearch.Request
cause: iOS 17 起对 MKLocalSearch.Request 的参数校验更严格，未设 `naturalLanguageQuery` 时直接返回空结果
fix: 创建 `MKLocalSearch.Request()` 后必须设置 `request.naturalLanguageQuery = "搜索词"`
