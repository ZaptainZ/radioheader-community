---
id: sw-ios-xcodegen-dev-team-regen
domain: iOS, Xcode, xcodegen
tags: xcodegen | DEVELOPMENT_TEAM | 签名 | signing | generate | 新文件 | 编译缺失 | project.yml
refs: topics/ios-swiftui.md
---
### xcodegen 常见陷阱：签名团队被清空 + 新文件不编译

symptoms: xcodegen generate 后签名配置丢失需重新选择 Team；新增 .swift 文件不参与编译

**签名团队**: `DEVELOPMENT_TEAM` 必须在 project.yml 中写死（`DEVELOPMENT_TEAM: YOUR_TEAM_ID`），否则每次 `xcodegen generate` 会清空该配置。

**新文件**: 添加新 .swift 文件后必须重新运行 `xcodegen generate`，否则文件不会加入 pbxproj 的编译 sources。
