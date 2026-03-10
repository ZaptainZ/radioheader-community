---
id: sw-ai-tool-failure-graceful-text
domain: AI, Tool Use, 容错
tags: 工具失败 | 搜索不可用 | tool execution error | 降级 | graceful degradation | 不阻断对话 | fallback
refs: topics/ai-api-integration.md
---
### 工具执行失败时返回友好文本给 LLM，不抛异常

symptoms: 外部 API 偶尔超时或返回错误，导致整个对话请求失败
context: LLM tool calling + 外部 API（搜索、地图等）
cause: 工具执行抛异常后没有 catch，错误沿调用链传播导致对话中断
fix: catch 所有工具执行异常，返回友好文本（如"搜索暂时不可用，请稍后再试"）作为 tool 消息内容；LLM 收到后会自行组织回答，对话不中断
