---
id: sw-python-subprocess-pipe-interactive
domain: Python, Subprocess, IPC
tags: 子进程交互 | subprocess pipe | select timeout | readline 阻塞 | 管道读取 | stdin stdout | 交互式程序 | drain output | first_timeout | line_timeout | 非阻塞读取 | PIPE | 小模型续写 | Human 截断
refs: topics/rust-systems.md
---
### 交互式子进程管道读取的超时与排空策略

symptoms: subprocess.Popen 的 stdout.readline() 永久阻塞，无法判断子进程是否已输出完毕
context: 需要通过 stdin/stdout 管道与交互式 CLI 程序（如本地 LLM 推理引擎）反复对话
cause: readline() 是阻塞调用，子进程空闲不输出时会无限等待
fix: 用 `select.select([proc.stdout], [], [], timeout)` 做超时检测再 readline。设计双超时参数：`first_timeout`（等首行，适配初始化/模型加载等慢操作，如 120s）和 `line_timeout`（等后续行，3s 无新输出视为"空闲"，排空完成）。循环读到超时即认为本轮输出结束。注意：子进程输出格式务必先用 `echo "test" | ./program` 实际观察，不要凭文档猜测
