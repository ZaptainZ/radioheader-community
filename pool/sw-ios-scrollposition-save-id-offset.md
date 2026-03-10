---
id: sw-ios-scrollposition-save-id-offset
domain: iOS, SwiftUI, UI
tags: 滚动位置 | scroll position | 恢复 | restore | 列表位置 | ScrollView | index 不准
refs: topics/ios-swiftui.md
---
### 滚动位置恢复应存 (itemId, yOffset) 而非 index

symptoms: 用 index 恢复滚动位置时偏移不准确，尤其是动态高度列表
context: SwiftUI 列表或 ScrollView 需要在返回或重新加载时恢复滚动位置
cause: index 不考虑行高差异，动态内容下同一 index 对应的像素位置会变化
fix: 保存 `(itemId, yOffset)` 对，恢复时先滚动到 itemId 再微调 offset
