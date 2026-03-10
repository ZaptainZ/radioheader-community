---
id: sw-claudecode-macos-bash3-no-assoc-array
domain: Shell, macOS, Bash
tags: declare -A | associative array | bash 3 | bash 4 | macOS | 关联数组 | 兼容性 | compatibility | mktemp
refs: topics/claude-code-meta.md
---
### macOS 默认 bash 3.2 不支持关联数组，CLI 脚本必须避免 bash 4+ 特性

symptoms: shell 脚本在 macOS 上报 `declare: -A: invalid option`，Linux 上正常
context: 用 `#!/bin/bash` 编写的 CLI 工具中使用了 `declare -A`（关联数组）
cause: macOS 自带 `/bin/bash` 是 v3.2（Apple 因 GPLv3 不升级），`declare -A` 需 bash 4+
fix: 用 `mktemp` 创建临时文件 + `grep ... | wc -l` 计数替代关联数组；或改用 `#!/usr/bin/env zsh`（macOS 默认 shell）。注意不要用 `grep -c`（有退出码陷阱，见 sw-shell-grep-c-exit-code-trap）
