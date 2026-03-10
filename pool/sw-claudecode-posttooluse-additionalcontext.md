---
id: sw-claudecode-posttooluse-additionalcontext
domain: Claude Code, Hooks, PostToolUse
tags: additionalContext | hook | 行为驱动 | Agent 指令 | 系统级注入 | 强制检查 | PostToolUse
refs: topics/claude-code-meta.md
---
### PostToolUse additionalContext 是驱动 Agent 行为的最强手段

symptoms: CLAUDE.md 规则写了但 Agent 不遵守，行为指令被忽略
context: 需要在特定工具操作后触发 Agent 执行检查流程
cause: CLAUDE.md 规则是"知识"，Agent 可能忽略；stdout 打印也可能被跳过
fix: PostToolUse hook 输出 JSON `{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"指令内容"}}`，内容作为系统级指令注入对话上下文
note: additionalContext > CLAUDE.md 规则 > stdout 打印（按 Agent 遵守强度排序）。**注意：additionalContext 只对 PostToolUse 和 UserPromptSubmit 有效，Stop hook 不支持——会报 JSON validation failed**
