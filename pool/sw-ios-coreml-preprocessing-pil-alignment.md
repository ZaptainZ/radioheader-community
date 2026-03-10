---
id: sw-ios-coreml-preprocessing-pil-alignment
domain: iOS, Core ML, Machine Learning
tags: Core ML | 预处理 | preprocessing | PIL | Python | 推理不准 | inference mismatch | 抗锯齿 | 灰度 | Y轴 | CNN | 置信度 | confidence | softmax
refs: topics/ios-swiftui.md
---
### Core ML 预处理必须对齐 Python PIL，否则推理结果偏差大

symptoms: 同一输入在 Python 和 iOS 上推理结果不同；iOS 端置信度或分类结果异常

**预处理 4 处差异**:
- 抗锯齿: iOS 默认开启，PIL 默认关闭 → 需关闭 iOS 侧抗锯齿
- 颜色空间: iOS 用 sRGB 转灰度有 gamma 差异 → 需直接以灰度模式处理
- 线端: iOS Core Graphics 默认 round cap，PIL 默认 butt cap → 设 `kCGLineCapButt`
- Y 轴: Core Graphics Y 轴向上，PIL Y 轴向下 → 绘制前翻转坐标

**CNN 置信度陷阱**: softmax 输出回答"输入最像哪个类别"，不是"输入质量好不好"。即使输入只有一个点，模型也可能输出 99.8% 置信度 → 不能用置信度做质量过滤
