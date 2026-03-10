---
id: sw-ios-xcode-debug-executable-whitescreen
domain: iOS, Xcode, Performance
tags: 白屏 | 启动慢 | white screen | slow launch | Debug executable | LLDB | 10s | 20s | 40s | 真机 | xcodegen | debugEnabled
refs: topics/ios-swiftui.md
---
### Xcode "Debug executable" 导致 iOS 真机启动白屏 10-40s

symptoms: iOS 真机运行时启动白屏 10-40s，模拟器正常或较快；Release 包无此问题
context: Xcode 默认开启 "Debug executable"，真机上 LLDB attach 后加载符号极慢
cause: LLDB 符号加载在 iOS 真机上耗时远超模拟器，阻塞 app 启动
fix: Edit Scheme → Run → Options → 取消勾选 "Debug executable"。xcodegen 项目需在**顶层 `schemes:` 块**配置 `debugEnabled: false`（target 内嵌的 `scheme:` 中设置不生效）
