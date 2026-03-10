---
id: sw-npu-rk3576-rk3588-model-incompatible
domain: NPU, Rockchip, RKLLM, Model Deployment
tags: RK3576 | RK3588 | rkllm | 模型不兼容 | NPU 核数 | w4a16 | w8a8 | target_platform | num_npu_core | 预转换模型 | HuggingFace | 推理失败 | model incompatible
refs: topics/product-hardware.md
---
### RK3576 和 RK3588 的 .rkllm 模型不通用

symptoms: RK3576 设备加载 HuggingFace 下载的 .rkllm 模型失败或推理异常；社区预转换模型全部标注 RK3588
context: Rockchip NPU 设备部署 LLM，使用 rkllm-toolkit 转换或下载预转换 .rkllm 文件
cause: RK3576 有 2 个 NPU 核心（量化 w4a16），RK3588 有 3 个核心（量化 w8a8）。模型文件内嵌了目标平台信息，不可跨平台使用。截至 2026-03，HuggingFace 上全部 115 个 RKLLM 预转换模型均为 RK3588
fix: 必须用 rkllm-toolkit 指定 `target_platform="rk3576"`, `num_npu_core=2`, `quantized_dtype="w4a16"` 重新转换。Qwen3-0.6B 转换后 692MB，推理正常
