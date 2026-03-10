---
id: sw-ios-xcassets-svg-imageset
domain: iOS, Xcode, Assets
tags: xcassets | svg | imageset | asset catalog | 编译错误 | build error | 图片资源
refs: topics/ios-swiftui.md
---
### Assets.xcassets 中裸露 SVG 文件导致 asset catalog 编译异常

symptoms: Xcode 构建时 asset catalog 编译报错或警告，SVG 图片无法正常显示
context: 直接将 .svg 文件放入 Assets.xcassets 目录，未创建 .imageset 文件夹
cause: Asset catalog 要求每个图片资源都在独立的 .imageset 目录中，含 Contents.json 描述文件；裸露的 svg 文件不被正确识别
fix: 为每个 SVG 创建对应的 .imageset 目录，包含 Contents.json（指定 `"filename": "xxx.svg"` + `"preserves-vector-representation": true`）
