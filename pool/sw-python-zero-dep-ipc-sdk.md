---
id: sw-python-zero-dep-ipc-sdk
domain: Python, IPC, SDK
tags: Unix socket | 零依赖 | zero dependency | 标准库 | stdlib | plugin SDK | 环境变量 | GeniePlugin | JSON Lines | 事件循环 | signal handler | SIGTERM
refs: topics/rust-systems.md
---
### Python 插件 SDK 可用纯标准库实现零外部依赖

symptoms: 需要在资源受限设备上运行 Python 插件，不想引入 pip 依赖
context: Python 3.9+ 环境，与 Rust 核心通过 Unix socket 通信
cause: asyncio/aiohttp 等库增加复杂度和内存占用，嵌入式环境 pip 安装不便
fix:
  - 用 `socket.AF_UNIX` + `socket.SOCK_STREAM` 直连，`json.dumps/loads` 处理 JSON Lines
  - 环境变量传参（`HOMEGENIE_SOCKET`=socket 路径, `HOMEGENIE_PLUGIN_ID`=插件标识），避免命令行解析
  - 基类模式：GeniePlugin 封装 connect → register → 事件循环 → 优雅关闭
  - `signal.signal(SIGTERM, handler)` 处理 kill 信号，`start_loop()` 中自动回复 ping
  - `on(method, handler)` 注册方法处理器，收到 request 自动调用并返回 response
  - 单个插件进程内存 ~20-30MB（含 Python 解释器），适合 4GB 设备并行运行多个
