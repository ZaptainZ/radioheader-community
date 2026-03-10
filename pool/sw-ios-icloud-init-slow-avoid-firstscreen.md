---
id: sw-ios-icloud-init-slow-avoid-firstscreen
domain: iOS, iCloud, Performance
tags: iCloud | 启动慢 | 白屏 | slow launch | 首屏 | 初始化 | CloudKit | UserDefaults | 同步 | 文档下载
refs: topics/ios-swiftui.md
---
### iOS iCloud 容器初始化慢，首屏路径必须完全避免 iCloud 调用

symptoms: app 启动时卡在加载、首屏空白，尤其在 iCloud 数据量大或网络慢时
context: iOS app 使用 iCloud 存储文档或配置数据

**初始化差异**: iOS 的 iCloud 容器初始化比 macOS 慢 3-10 倍，且 iOS 不会自动下载远端文档（macOS 会）

**首屏优化**:
- 首屏渲染路径必须完全避免 iCloud 调用（包括读取 iCloud KV store）
- Settings/偏好存 UserDefaults（非 NSUbiquitousKeyValueStore），消除启动路径的 iCloud 依赖
- iCloud 数据加载放到后台，首屏用本地缓存或 skeleton UI

**注意**: iCloud 同步可能卡住 git 仓库（.git 目录被同步），项目目录应排除 iCloud 或保持远端备份
