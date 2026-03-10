---
id: sw-ai-chatgpt-plus-not-api-credits
domain: AI, OpenAI, OAuth, ChatGPT
tags: ChatGPT Plus | API credits | insufficient_quota | 配额不足 | 429 | billing | 计费分离 | codex responses | backend-api | gpt-5.3-codex | 订阅 vs API
refs: topics/ai-api-integration.md
---
### ChatGPT Plus 订阅与 OpenAI API credits 是完全独立的计费系统

symptoms: 用 OAuth 拿到的 token 调 `api.openai.com/v1/chat/completions` 返回 `insufficient_quota` 或 429
context: 通过 OpenAI OAuth PKCE 获取 access_token（ChatGPT Plus 用户），尝试调用标准 API
cause: ChatGPT Plus 订阅只授权使用 `chatgpt.com/backend-api/` 端点，与 `api.openai.com/v1/` 的 API credits 完全独立
fix: 使用 `POST https://chatgpt.com/backend-api/codex/responses`，model=`gpt-5.3-codex`，body 格式 `{model, instructions, input:[{role,content}], store:false, stream:true}`，header 需 `ChatGPT-Account-Id`。SSE 事件 `response.output_text.delta` 含 `{"delta":"text"}`，`response.completed` 结束。
