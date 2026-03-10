---
id: sw-ai-gemini-tool-choice-long-prompt
domain: AI, Gemini, Tool Use
tags: tool_choice | 工具不调用 | tool not called | auto 失效 | required | 长提示 | long prompt | function calling
refs: topics/ai-api-integration.md
---
### Gemini 长系统提示下 tool_choice auto 几乎不主动调工具

symptoms: 配置了工具定义，但模型始终用文本回答，从不调用工具
context: Gemini API + 较长的 system prompt + `tool_choice: "auto"`
cause: 长系统提示占据模型注意力，auto 模式下模型倾向用已有上下文回答而非调用外部工具
fix: 改用 `tool_choice: "required"` 强制模型必须调用工具
