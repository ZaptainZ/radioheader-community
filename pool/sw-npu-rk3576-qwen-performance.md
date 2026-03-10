---
id: sw-npu-rk3576-qwen-performance
domain: NPU, RK3576, AI
tags: RK3576 | Qwen3 | 0.6B | w4a16 | 692MB | NPU 推理 | 500ms | 首 token | RKLLama | 轻量 wrapper
refs: topics/product-hardware.md
---
### RK3576 NPU 推理实测：Qwen3-0.6B 首 token ~500ms

context: 在 RK3576 SBC 上部署本地 LLM
fix:
- Qwen3-0.6B w4a16 转换后 692MB，R76S NPU 推理正常
- 首 token 延迟 ~500ms
- RKLLama（Ollama for Rockchip）依赖 torch/opencv/piper-tts，4GB 设备装不下
- 需自写轻量 wrapper 调用 rkllm 推理，不用 RKLLama
