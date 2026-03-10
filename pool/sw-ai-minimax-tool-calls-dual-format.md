---
id: sw-ai-minimax-tool-calls-dual-format
domain: AI, MiniMax, Tool Use
tags: tool_calls | MiniMax | M2.5 | 工具调用解析 | XML格式 | JSON格式 | function calling | 三种格式 | tool_calls数组 | <tool_calls>标签 | <minimax:tool_call> | invoke | 原始XML显示 | 工具调用不触发
refs: topics/ai-api-integration.md
---
### MiniMax tool_calls 返回三种格式，必须全部处理

symptoms: tool calling 集成后部分请求工具调用正常、部分被忽略；未匹配格式的原始 XML 标签直接显示给终端用户
context: MiniMax M2.5 API + OpenAI 兼容格式 + 工具定义
cause: MiniMax 返回三种 tool_calls 格式：A) 标准 JSON `message.tool_calls[]`；B) XML `<tool_calls>{"name":"xxx","arguments":{...}}</tool_calls>` 嵌入 content；C) `<minimax:tool_call><invoke name="xxx"><parameter name="yyy">zzz</parameter></invoke></minimax:tool_call>` 嵌入 content
fix: 按优先级依次检查三种格式：1) 响应 JSON 中 `tool_calls` 数组；2) 正则 `<tool_calls>(.*?)</tool_calls>` 解析 content；3) 正则 `<minimax:tool_call>(.*?)</minimax:tool_call>` + `<invoke name="(.*?)">` + `<parameter name="(.*?)">(.*?)</parameter>` 解析 content。匹配后清除 content 中的 XML 标签。格式 B 的 arguments 可能是对象而非字符串，需兼容处理
