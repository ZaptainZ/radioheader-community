---
id: sw-npu-colima-rosetta-x86-toolkit
domain: macOS, colima, Rosetta, Linux Tooling
tags: colima | Rosetta 2 | x86_64 | ARM64 | rkllm-toolkit | vz-rosetta | libc6 amd64 | archive.ubuntu.com | ports.ubuntu.com | 动态链接器 | ld-linux-x86-64 | binfmt | 模型转换 | macOS 跑 x86 Linux 工具
refs: topics/product-hardware.md
---
### macOS 通过 colima + Rosetta 运行 x86_64-only Linux 工具

symptoms: 某些 ML 工具（如 rkllm-toolkit）仅提供 x86_64 Linux wheel，macOS 无法直接 pip install
context: Apple Silicon Mac 需要运行只有 x86_64 Linux 二进制的 Python 工具
cause: 工具厂商未提供 ARM64 或 macOS 构建
fix:
1. `colima start --arch aarch64 --vm-type vz --vz-rosetta --cpu 4 --memory 8`（**不能** `--arch x86_64`，否则需 QEMU）
2. VM 内：`dpkg --add-architecture amd64` + 添加 `archive.ubuntu.com` 源（**不是** `ports.ubuntu.com`，后者无 amd64 包）+ `apt install libc6:amd64`
3. 安装 x86_64 Miniconda → `conda install python=3.10` → pip install x86 wheel
4. 注意 colima 会缓存上次配置，切换架构需 `colima delete --force` 重建
