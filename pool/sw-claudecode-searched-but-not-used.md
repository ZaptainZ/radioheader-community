---
id: sw-claudecode-searched-but-not-used
domain: Claude Code, Agent Behavior, Knowledge Management
tags: 搜到没用 | 搜到但跳过 | found but ignored | 经验命中 | 搜→用→追 | 行为规则 | 回流失败
refs: topics/claude-code-meta.md
---
### "搜到但没用"比"搜不到"更危险

symptoms: Agent 搜索了知识库、命中了相关经验，但回复中完全没引用，直接做独立分析
context: 知识库中已有解决过的经验，Agent 被要求"先搜索"
cause: "必须搜索"的规则只约束了搜索动作，没约束搜到后的行为。Agent 将搜索结果当背景信息过滤掉
fix: 将规则升级为三步强制流程——搜（搜索）→ 用（命中必须引用并验证适用性）→ 追（需要细节时追溯到源项目）。显式禁止"搜到不用"
