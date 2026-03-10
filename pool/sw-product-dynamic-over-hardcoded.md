---
id: sw-product-dynamic-over-hardcoded
domain: Product, UX
tags: 动态参数 | 硬编码 | min() | 上限 | 阻尼 | damping | 用户偏好 | 可扩展
refs: topics/product-hardware.md
---
### 动态/可扩展方案优于硬编码，离群参数用动态阻尼

symptoms: 用户明确反对 min() 硬上限，认为不够灵活
context: 参数设计中需要限制极端值
cause: 硬编码上限（如 `min(value, 100)`）无法适应所有场景
fix: 用动态阻尼函数代替硬上限——值越偏离中心衰减越大，但不设绝对天花板。整体设计原则：动态/可扩展方案优于硬编码
