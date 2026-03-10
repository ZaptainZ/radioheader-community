---
id: sw-ios-coreml-derived-data-cache
domain: iOS, Core ML, Xcode
tags: Core ML | DerivedData | 崩溃 | crash | mlmodelc | 缓存 | cache | 模型更新 | inference error
refs: topics/ios-swiftui.md
---
### Core ML 模型更新后必须清 DerivedData 否则推理崩溃

symptoms: 更新 .mlmodel 文件后运行 app 崩溃或推理结果异常
context: Xcode 项目中替换或更新了 Core ML 模型文件
cause: Xcode 缓存旧的 mlmodelc（编译后模型），模型输出名或结构变化后仍用旧缓存，导致运行时类型不匹配
fix: 更新 Core ML 模型后执行 `rm -rf ~/Library/Developer/Xcode/DerivedData/{项目名}*`，然后 Clean Build（Cmd+Shift+K）再运行
