---
id: sw-ios-pbxproj-group-filesystem-mismatch
domain: iOS, Xcode
tags: pbxproj | Group | 文件缺失 | file not found | 编译 | compile sources | 手动编辑 | Xcode 项目
refs: topics/ios-swiftui.md
---
### pbxproj Group 与文件系统不一致时新文件不参与编译

symptoms: 新增的 .swift 文件在 Xcode 中可见但编译时报 "undeclared" 或类型找不到
context: 手动在文件系统添加文件，或 Xcode 项目 Group 结构与实际文件夹不一致
cause: Xcode 的 pbxproj 按 Group 结构维护编译 sources 列表，文件系统中存在但未加入 pbxproj 的文件不会被编译
fix: 在 Xcode 中右键 Group → Add Files to Project 添加文件，或手动编辑 pbxproj 将文件加入对应 target 的 Compile Sources
