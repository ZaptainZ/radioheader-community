---
id: sw-ai-two-phase-tool-stream
domain: AI, LLM, Tool Use
tags: tool use | 两阶段 | two-phase | 流式 | streaming | 工具循环 | 工具调用后回答
refs: topics/ai-api-integration.md
---
### 工具调用采用两阶段流程：非流式工具循环 + 流式回答

symptoms: 流式输出中夹杂工具调用导致前端处理复杂、显示异常
context: LLM 应用同时需要工具调用和流式回答
cause: 工具调用结果需要完整 JSON 才能解析和执行，与流式 token 输出混合会增加解析复杂度
fix: Phase 1 非流式工具循环（调用工具 → 获取结果 → 决定是否继续调用），Phase 2 拿到所有工具结果后再流式输出最终回答
