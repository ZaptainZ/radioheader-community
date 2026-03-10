---
id: sw-net-ssh-agent-noninteractive
domain: Networking, SSH, Git
tags: SSH | ssh-agent | ssh-add | GitHub | permission denied | 非交互 | key not loaded | git push 失败
refs: topics/networking-proxy.md
---
### SSH key 添加到 GitHub 后仍需手动加载 ssh-agent

symptoms: `git push` 或 SSH 连接报 `Permission denied (publickey)`，尽管 key 已在 GitHub 设置中
context: 新终端会话或非交互 SSH 连接
cause: 非交互 SSH 会话不自动加载 ssh-agent，key 文件存在但未被 agent 托管
fix: `eval $(ssh-agent -s) && ssh-add ~/.ssh/id_ed25519`。永久方案：在 `~/.ssh/config` 中加 `AddKeysToAgent yes` + macOS 加 `UseKeychain yes`
