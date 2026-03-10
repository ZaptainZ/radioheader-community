---
id: sw-ai-on-device-inference-sizing
domain: AI, Edge, NPU, Deployment
tags: 端侧推理 | on-device | NPU | RK3576 | 4GB | 小模型 | Qwen2 | 0.5B | 1.8B | token/s | 模型部署
refs: topics/ai-api-integration.md
---
### 端侧推理模型选型：4GB SBC 舒适区 0.5B-1.8B

symptoms: 需要在低功耗设备上本地运行 LLM，不确定模型大小选择
context: 4GB 内存 ARM SBC（如 RK3576/RK3588）上部署本地 LLM

**性能参考**: Qwen2 0.5B 在 RK3576 NPU 上 ~34 t/s，适合意图分类、简单对话

**选型建议**: 4GB 设备舒适区为 0.5B-1.8B 参数模型，超过 3B 会明显受限于内存

**部署架构**: 端上推理（速度）+ 服务端训练（改进）+ 按需分发（增量更新）。渐进实施路径：先嵌入完整模型 → 骨干/头分离 → 全量架构
