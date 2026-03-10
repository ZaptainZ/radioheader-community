---
id: sw-ai-tool-message-fields-required
domain: AI, Tool Use, OpenAI-compatible API
tags: tool_call_id | tool message | role tool | 400错误 | API拒绝 | 消息格式 | function calling | assistant tool_calls 透传
refs: topics/ai-api-integration.md
---
### Tool 结果消息必须携带 tool_call_id + name，assistant 消息必须透传 tool_calls

symptoms: 工具执行成功但提交结果时 API 返回 400 错误
context: OpenAI 兼容格式的 chat completions API + 多轮工具调用
cause: `role: "tool"` 消息缺少 `tool_call_id` 或 `name` 字段；或前序 `role: "assistant"` 消息未包含完整的 `tool_calls` 数组
fix: tool 消息同时设置 `tool_call_id`（对应 assistant 返回的 call ID）和 `name`（函数名）；assistant 消息原样透传 `tool_calls` 数组到下一轮请求
