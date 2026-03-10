---
id: sw-rust-cross-platform-ping-timeout
domain: Rust, Networking, Linux, macOS
tags: ping | -W | timeout | 超时 | 跨平台 | gateway | 网关检测 | ICMP | network monitor | 断网 | offline
refs: topics/rust-systems.md
---
### macOS 与 Linux 的 ping -W 含义不同

symptoms: macOS 上 `ping -c 1 -W 2` 总是失败（即使网关正常），Linux 正常
context: 用 tokio::process::Command 运行 ping 做网络检测
cause: `-W` 在 Linux 是秒（`-W 2` = 2s），macOS 是毫秒（`-W 2` = 2ms，必超时）
fix: 不依赖 ping 结果做最终判断。ping 失败后继续做 DNS lookup + HTTP HEAD 补救——某些网关本身不响应 ICMP，ping 失败 ≠ 离线。三级检测链：ping 网关 → DNS resolve → HTTP HEAD（各级 2-3s 超时），区分 Online / LocalOnly / Offline
