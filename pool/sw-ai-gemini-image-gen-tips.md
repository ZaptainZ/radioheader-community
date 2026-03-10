---
id: sw-ai-gemini-image-gen-tips
domain: AI, Gemini, Image Generation
tags: Gemini | 图像生成 | image generation | flash-image-preview | 参考图 | style_ref | 多余手指 | extra hands | prompt 技巧 | JPEG 压缩
refs: topics/ai-api-integration.md
---
### Gemini 图像生成的参考图、风格控制与常见问题

symptoms: 生成图片风格不一致、多余手指/物体、参考图传入失败或效果差
context: 使用 Gemini `gemini-3.1-flash-image-preview` 模型生成图像，region 需设为 `global`

**参考图**: 需压缩至 ~200KB JPEG（macOS 可用 `sips` 工具），过大的图片影响生成质量和速度

**风格一致性**: style_ref 机制——用之前生成的成功结果作为参考图传入，显著提升风格一致性

**约束违规**: prompt 中使用 "IMPORTANT/CRITICAL + 否定句"（如 "CRITICAL: do NOT add extra fingers"）对约束 AI 违规行为有效

**多手/多余物体**: AI 图像生成常见问题，需在 prompt 中显式否定（"no extra hands, no duplicate objects"）
