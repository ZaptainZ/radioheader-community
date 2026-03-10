---
id: sw-rust-subprocess-output-format
domain: Rust, Python, Subprocess
tags: 子进程 | subprocess | 输出格式 | 先测试 | echo | 不要猜 | 解析
refs: topics/rust-systems.md
---
### 子进程输出解析必须先用 echo 测试实际格式，不要猜

symptoms: 子进程输出解析逻辑写好后解析失败或提取到错误内容
context: Rust/Python 调用外部程序并解析 stdout 输出
cause: 假设了输出格式（如每行一条），实际格式可能完全不同（如 `user: <echo> robot: <response>` 同一行）
fix: 开发前先用 `echo "test" | ./program` 观察实际输出格式，基于实际格式编写解析逻辑
