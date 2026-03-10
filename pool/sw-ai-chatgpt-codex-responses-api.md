---
id: sw-ai-chatgpt-codex-responses-api
domain: AI, OpenAI, ChatGPT
tags: Codex | Responses API | ChatGPT Plus | SSE | gpt-5.3-codex | ChatGPT-Account-Id | OAuth | backend-api
refs: topics/ai-api-integration.md
---
### ChatGPT Plus 的 Codex Responses API 使用方式

context: 使用 ChatGPT Plus 订阅（非 OpenAI API credits）调用编程模型
fix:
- 端点: `chatgpt.com/backend-api/codex/responses`（不是 `api.openai.com`）
- model: `gpt-5.3-codex`
- body: `{model, instructions, input:[{role,content}], store:false, stream:true}`
- header 必须包含 `ChatGPT-Account-Id`
- SSE 格式: `event: response.output_text.delta` + `data: {"delta":"text"}`，结束信号 `event: response.completed`
- OAuth CLIENT_ID: `app_EMoamEEZ73f0CkXaXp7hrann`（OpenClaw/Codex CLI 公共 client）
