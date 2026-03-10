---
id: sw-ai-llm-inline-tag-extraction
domain: AI, LLM, Backend
tags: 结构化提取 | structured extraction | 内联标签 | inline tag | JSON 解析失败 | parse error | 对话+提取 | one-call | ##TAG## | cleanReply | 静默跳过
refs: topics/ai-api-integration.md
---
### LLM 回复末尾内联标签提取结构化数据

symptoms: 需要从对话回复中同时提取结构化信息（用户画像、情感、意图等），不想多次调用 LLM
context: 任何需要"对话 + 元数据提取"的 AI 聊天系统
fix: system prompt 中指示 LLM 在回复末尾用自定义标签包裹 JSON（如 `##TAG##{"key":"value"}##/TAG##`），后端正则提取后 cleanReply 去除标签再返回用户
caveats:
- LLM 输出 JSON 不稳定（多余逗号、字段缺失、截断），解析失败必须 warn 级别静默跳过，不能阻断主对话流
- 提取指令必须写明"没有新信息则不输出此标签"，否则 LLM 每次都生成空 JSON 浪费 tokens
- 正则用 `(?s)` (DOTALL) 模式匹配跨行 JSON
