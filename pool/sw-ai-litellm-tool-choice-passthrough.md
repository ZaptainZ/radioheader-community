---
id: sw-ai-litellm-tool-choice-passthrough
domain: AI, LiteLLM, Backend
tags: LiteLLM | tool_choice | Pydantic | 字段丢失 | 静默丢弃 | silent drop | 工具不调用 | schema | 透传
refs: topics/ai-api-integration.md
---
### LiteLLM 后端必须完整透传 tool_choice，Pydantic schema 漏字段会静默丢弃

symptoms: LLM 不主动调用工具，或 tool_choice 设置不生效
context: 后端通过 LiteLLM 代理调用多种 LLM API，使用 Pydantic model 定义请求结构
cause: Pydantic schema 未显式定义 `tool_choice` 字段时会静默丢弃该参数，LiteLLM 收到的请求中不含 tool_choice
fix: 确保 Pydantic model 中显式声明 `tool_choice: Optional[str] = None` 字段，或用 `model_config = ConfigDict(extra="allow")` 允许透传额外字段
