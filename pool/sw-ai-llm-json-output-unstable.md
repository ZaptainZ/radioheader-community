---
id: sw-ai-llm-json-output-unstable
domain: AI, LLM, Parsing
tags: LLM | JSON | 解析失败 | parse error | 多余逗号 | 截断 | truncated | 格式不稳定 | 静默跳过
refs: topics/ai-api-integration.md
---
### LLM 输出 JSON 格式不稳定，解析失败必须静默跳过

symptoms: JSON.parse 异常、多余逗号、截断的 JSON 字符串
context: 让 LLM 在回复中输出结构化 JSON（如内联标签提取）
cause: LLM 不保证输出严格合法的 JSON，尤其在长输出或 token 限制下会截断
fix: 解析失败时用 warn 级别日志记录但不抛异常，不影响主对话流。提取指令中明确写"没有新信息则不输出此标签"避免 LLM 每次都生成空 JSON 浪费 tokens
