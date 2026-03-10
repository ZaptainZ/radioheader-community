---
id: sw-claudecode-memory-layout
domain: Claude Code, Memory
tags: Claude Code | memory | MEMORY.md | 200 行 | 截断 | 项目记忆 | 会话上下文 | CLAUDE.md | 自动注入
refs: topics/claude-code-meta.md
---
### Claude Code 记忆系统布局与自动注入规则

context: 理解 Claude Code 的记忆如何加载
fix:
- 项目记忆: `~/.claude/projects/{path}/memory/`，每个项目隔离
- `MEMORY.md` 前 200 行自动注入会话上下文，超过截断——关键信息必须放前 200 行
- 全局 `~/.claude/CLAUDE.md` 前 200 行也自动加载
- 全局 hooks: `~/.claude/hooks/`，项目 hooks: `{项目}/.claude/hooks/`
