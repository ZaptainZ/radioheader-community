---
id: sw-ios-appstore-review-pitfalls
domain: iOS, App Store, Review
tags: App Store | 审核 | 被拒 | rejection | 位置权限 | location | 隐藏功能 | hidden UI | APPSTORE_REVIEW | 编译标志 | Token | 登录
refs: topics/ios-swiftui.md
---
### App Store 审核常见被拒原因与防范

symptoms: 提交审核被拒，收到 Guideline violation

**位置权限**: NSLocationWhenInUseUsageDescription 必须包含具体用途 + 使用示例（如"用于在地图上显示您附近的餐厅"），不能只写"提供定位服务"。

**隐藏功能**: tap 10 次等隐藏 UI 操作会触发 Guideline 2.3.1 被拒。调试功能必须用编译标志控制，不进入提审包。

**编译标志**: `APPSTORE_REVIEW` 等自定义编译标志必须同时加在 Debug **和 Release** 配置中，否则 Release 包中条件编译失效。

**审核账号**: 提供给审核团队的测试账号必须走正常 API 登录流程生成真实 Token，不能在客户端硬编码 Token 绕过认证。
