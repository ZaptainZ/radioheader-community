---
id: sw-ai-llm-infer-location-from-history
domain: AI, LLM, Geolocation
tags: 位置推断 | 历史数据 | location inference | system prompt | 上下文注入 | 用户动态 | 当前位置猜测 | context injection | historical data
refs: topics/ai-api-integration.md
---
### LLM 会从历史数据推断用户当前位置（错误）

symptoms: AI 对用户说"你最近是不是在XX"，但用户实际不在那里；AI 把历史发布记录当作当前位置依据
context: system prompt 中注入了用户历史内容（含地理信息），LLM 自动关联推断用户当前所在地
fix:
- 历史数据段落必须明确标注"历史记录，不代表当前位置"（header + footer 双标注）
- 无 GPS 时声明"定位不可用，请勿猜测用户所在城市"
- 当前位置信息单独分段（"== 当前上下文 =="），与历史数据段落物理隔离
- 在 system prompt 规则中显式禁止："绝对不要从历史动态中推断用户现在在哪里"
