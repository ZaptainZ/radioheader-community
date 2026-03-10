---
id: sw-ios-urlsession-bytes-slow
domain: iOS, Swift, Networking
tags: URLSession | bytes | 下载慢 | slow download | 进度追踪 | progress | async 开销 | 性能 | performance
refs: topics/ios-swiftui.md
---
### URLSession.bytes(from:) 逐字节迭代做进度追踪极慢

symptoms: 下载进度追踪功能导致下载速度异常慢，CPU 占用高
context: 用 `URLSession.bytes(from:)` 的 async for-in 循环逐字节统计下载进度
cause: 5MB 文件 = 500 万次 async 迭代，async/await 调度开销远超 I/O 本身
fix: 改用 `URLSession.download(from:delegate:)` + `URLSessionDownloadDelegate` 的 `didWriteData` 回调报告进度
