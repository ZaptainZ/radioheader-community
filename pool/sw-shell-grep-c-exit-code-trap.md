---
id: sw-shell-grep-c-exit-code-trap
domain: Shell, Bash
tags: grep -c | exit code | set -e | 整数表达式 | integer expression expected | wc -l | 计数 | count | 匹配数为零 | zero matches
refs: topics/claude-code-meta.md
---
### grep -c 匹配 0 行时退出码为 1，在 set -e 下导致变量值异常

symptoms: shell 脚本报 `integer expression expected`，或 `[ "$var" -eq 0 ]` 失败，变量实际值是 `"0\n0"` 两行
context: 在 `set -e` 的脚本中用 `$(grep -c PATTERN file || echo "0")` 获取匹配行数
cause: `grep -c` 匹配 0 行时输出 "0" 但退出码为 1（非零），`|| echo "0"` 被触发再追加一个 "0"，变量变成两行 `"0\n0"`
fix: 改用 `grep PATTERN file | wc -l | tr -d ' '`。`wc -l` 对空输入返回 0 且退出码始终为 0，不触发 `set -e`
