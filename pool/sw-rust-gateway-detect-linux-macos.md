---
id: sw-rust-gateway-detect-linux-macos
domain: Rust, Networking, Linux, macOS
tags: gateway | 网关 | ip route | netstat | default route | 默认路由 | detect | 跨平台
refs: topics/rust-systems.md
---
### 跨平台默认网关检测

symptoms: 需要获取默认网关 IP 做连通性检测
context: Rust 异步进程中通过 tokio::process::Command 调用系统命令
fix: 先尝试 Linux 命令，失败再 macOS：
  1. Linux: `ip route show default` → 解析 "default via x.x.x.x dev ethN" 第 3 列
  2. macOS: `netstat -rn` → 找 "default" 开头行，取第 2 列
  两者输出格式不同，不可混用解析逻辑
