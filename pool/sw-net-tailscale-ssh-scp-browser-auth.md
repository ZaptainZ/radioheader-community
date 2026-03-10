---
id: sw-net-tailscale-ssh-scp-browser-auth
domain: Networking, Tailscale, SSH
tags: Tailscale | SSH | scp | 浏览器认证 | browser auth | 超时 | timeout | 远程开发
refs: topics/networking-proxy.md
---
### Tailscale SSH/scp 首次连接需浏览器认证，可能超时

symptoms: Tailscale SSH 或 scp 首次连接卡住后超时
context: 通过 Tailscale 网络 SSH 连接远程设备
cause: Tailscale SSH 的 scp 也需要浏览器认证流程，首次未完成认证时连接超时
fix: 首次连接超时后重试，确保在浏览器中完成 Tailscale 认证。远程开发服务器通过 Tailscale IP 访问
