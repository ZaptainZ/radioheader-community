---
id: sw-claudecode-five-step-lookup
domain: Claude Code, Knowledge Management
tags: 信息查找 | lookup | 搜索策略 | Explore | Grep | RadioHeader | CLAUDE.md | 五步
refs: topics/claude-code-meta.md
---
### 五步信息查找策略：禁止跳过前面步骤直接 Explore

context: Agent 在项目中查找信息的优先级

fix:
1. 检查已加载上下文（MEMORY.md 已自动注入）
2. 查 CLAUDE.md 索引定位文档
3. 搜 RadioHeader（全局经验）
4. Grep/Glob 针对性搜索
5. Explore（最后手段，必须限定范围）

**禁止**: 跳过 1-4 直接启动 Explore——浪费时间且结果发散
