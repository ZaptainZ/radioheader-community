---
id: sw-ssh-host-key-changed-after-reflash
domain: SSH, DevOps
tags: REMOTE HOST IDENTIFICATION HAS CHANGED | host key | known_hosts | 刷机 | Permission denied | man-in-the-middle | reflash
refs: topics/product-hardware.md
---
### 刷机后 SSH 报 HOST IDENTIFICATION HAS CHANGED

symptoms: SSH 连接报 "REMOTE HOST IDENTIFICATION HAS CHANGED" + "Permission denied"
context: 对同一 IP 的设备重装系统后，新系统生成了新的 SSH host key
cause: known_hosts 中缓存了旧系统的 host key，新系统 key 不匹配，SSH 拒绝连接且禁用密码认证
fix: `ssh-keygen -R <ip>` 清除旧条目，然后正常连接即可
