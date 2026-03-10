---
id: sw-ai-clear-chat-purge-history
domain: AI, LLM, Chat
tags: 清除聊天 | clear chat | 历史记录 | 编造回答 | hallucination | 持久化 | context pollution | 上下文污染
refs: topics/ai-api-integration.md
---
### 清除聊天时必须同时清除持久化历史，否则旧编造回答被重新注入

symptoms: 用户清除聊天后新对话中 LLM 仍然引用之前的错误信息或编造内容
context: 聊天应用将对话历史持久化到数据库/文件
cause: UI 上的"清除聊天"只清了前端显示，后端持久化的历史消息未删除，下次加载时旧消息（含之前的编造回答）重新注入 LLM 上下文
fix: 清除聊天时必须同时删除后端持久化的消息记录，包括 assistant 消息、tool 消息和用户消息
