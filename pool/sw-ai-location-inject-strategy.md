---
id: sw-ai-location-inject-strategy
domain: AI, LLM, Geolocation
tags: 位置注入 | location | system prompt | CLGeocoder | 缓存 | Redis | 实时数据 | 位置感知
refs: topics/ai-api-integration.md
---
### LLM 位置数据注入策略：实时附带 > 缓存 fallback > 无位置

symptoms: LLM 不知道用户位置，或位置数据过期导致回答不准确
context: AI 聊天应用需要位置感知能力
fix:
- 优先级：请求实时附带（客户端每次请求带坐标）> Redis/缓存后台上报 > 无位置
- 坐标先经 CLGeocoder 转为地址文字再注入 system prompt（LLM 无法准确解析原始经纬度）
- CLGeocoder 有频率限制，按距离缓存（~500m 阈值）避免重复调用
