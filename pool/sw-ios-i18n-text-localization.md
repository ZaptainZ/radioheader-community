---
id: sw-ios-i18n-text-localization
domain: iOS, SwiftUI, i18n
tags: 本地化 | localization | i18n | Text | LocalizedStringKey | String(localized:) | navigationTitle | LocalizedError | 翻译不生效 | 国际化
refs: topics/ios-swiftui.md
---
### SwiftUI 本地化三个易错点：Text 变量、navigationTitle、LocalizedError

symptoms: 部分文本翻译不生效，字符串显示原文而非本地化版本

**Text 字面量 vs 变量**: `Text("Hello")` 字面量自动本地化；`Text(someVar)` 变量不自动本地化，需 `Text(LocalizedStringKey(someVar))` 或传入 `LocalizedStringKey` 类型。非 SwiftUI 环境用 `String(localized: "key")`。

**navigationTitle**: `.navigationBarTitle("X", displayMode: .inline)` 不自动本地化（参数类型是 String 非 LocalizedStringKey），改用 `.navigationTitle("X")` 即可自动本地化。

**LocalizedError**: `LocalizedError.errorDescription` 返回 `String?`，不会自动走本地化查找。需手动返回 `String(localized: "error.description")`。
