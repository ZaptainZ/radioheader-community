---
id: sw-arm64-pytorch-illegal-instruction
domain: ARM64, ML, Python
tags: PyTorch | torch | Illegal instruction | SIGILL | ARM64 | aarch64 | RK3576 | Rockchip | SBC | onnxruntime | sentence-transformers | embedding | 嵌入式 | NPU
refs: topics/rust-systems.md
---
### PyTorch 在部分 ARM64 SoC 上 Illegal instruction，用 onnxruntime 替代

symptoms: `python3 -c "import torch"` 或 `from sentence_transformers import SentenceTransformer` 崩溃，exit code 132，bash 报 Illegal instruction
context: ARM64 嵌入式设备（如 RK3576），pip 安装了 torch + sentence-transformers
cause: PyTorch wheel 使用了目标 SoC 不支持的 CPU 指令（某些 NEON/SVE 扩展）。pip 安装的 aarch64 wheel 是通用编译的，不保证兼容所有 ARM64 芯片
fix: 绕过 torch，直接用 onnxruntime + tokenizers 加载 ONNX 格式模型。以 MiniLM 句子编码为例：下载 HuggingFace 上的 `onnx/model.onnx` + `tokenizer.json`，用 tokenizers 库做分词，onnxruntime 做推理，手动 mean pooling + L2 归一化。ARM64 CPU 上 ~85ms/2句（384维），无 torch 依赖
