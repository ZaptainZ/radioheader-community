---
id: sw-rust-sensitive-content-filter
domain: Rust, Security, Memory, LLM
tags: 敏感信息过滤 | sensitive filter | API Key 泄漏 | 记忆提取 | memory extraction | sk- 前缀 | 密码 | password | secret | token | Bearer | 私钥 | 日志脱敏 | PII
refs: topics/rust-systems.md
---
### 用户输入记忆提取前过滤敏感信息

symptoms: 用户在对话中说"请记住我的密码是xxx"或"我的 key 是 sk-xxx"，系统自动提取并持久化了敏感信息
context: AI 对话系统自动从用户消息中提取记忆（偏好、身份等）写入数据库
cause: 记忆提取逻辑只匹配模式（"请记住"/"我的xxx是"），不检查内容是否敏感
fix: 在 `engine.add()` 前调用 `contains_sensitive()` 检查。前缀匹配：`sk-`、`key-`、`-----BEGIN`、`Bearer `。关键词匹配（大小写不敏感）：`密码是`、`password:`、`secret=`、`token:`、`pwd=` 等。命中则跳过提取，仅记 info 日志
