---
id: sw-claudecode-new-session-read-first
domain: Claude Code, Best Practices
tags: 新会话 | new session | 先读后做 | 偏离目标 | 不读文档 | 血的教训
refs: topics/claude-code-meta.md
---
### 新会话开始时不读文档就操作 = 偏离目标

symptoms: Agent 在新会话中做出与项目方向不一致的修改
context: Claude Code 新会话开始，Agent 直接执行用户请求而未先了解项目上下文
cause: 没有先读 CLAUDE.md、MEMORY.md 和相关文档就动手，对项目状态的假设可能错误
fix: 新会话必须先检查已加载上下文（MEMORY.md 自动注入），按需查阅 CLAUDE.md 索引中的文档，再开始操作
