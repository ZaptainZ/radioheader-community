---
id: sw-ai-system-prompt-file-preview-hallucinate
domain: AI, LLM, Prompt Engineering
tags: system prompt | 文件预览 | hallucination | 编造 | 幻觉 | 上下文注入 | file preview | 已有内容
refs: topics/ai-api-integration.md
---
### system prompt 中的文件预览会让 LLM 误以为已有内容而编造回答

symptoms: LLM 回答中包含文件的"内容摘要"或"分析"，但实际文件内容与回答不符
context: 在 system prompt 中注入文件名列表或文件预览信息
cause: LLM 看到文件名/预览后推测文件内容，以高置信度编造出看似合理的回答
fix: system prompt 中只提供文件名和元数据，明确标注"以下仅为文件名列表，你尚未读取文件内容"，或等用户明确请求后再通过 tool use 获取实际内容
