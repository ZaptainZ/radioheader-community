---
id: sw-ai-llm-cannot-reverse-geocode
domain: AI, LLM, iOS, Geolocation
tags: 反向地理编码 | reverse geocode | 经纬度 | lat lng | 位置不准 | 猜错城市 | CLGeocoder | system prompt 位置 | 地址文字 | 坐标转地址
refs: topics/ai-api-integration.md
---
### LLM 无法从原始坐标准确推断地理位置

symptoms: 在 system prompt 中注入纬度/经度数值，LLM 回复中猜错城市或区县（如北京平谷 → 天津武清）
context: AI 聊天应用需要位置感知能力，将用户坐标注入 LLM 上下文
fix: 客户端先用 Geocoding API（iOS CLGeocoder / Android Geocoder / Google Maps API）将坐标转为地址文字，再注入 system prompt。原始坐标仅作 fallback
caveats:
- CLGeocoder 有频率限制，按距离缓存（~500m 阈值）避免重复调用
- CLGeocoder 只返回行政地址（省市区街道），不返回 POI 名称（商场/小区），POI 需用 MKLocalSearch 补充
- 位置数据优先级：请求实时附带 > Redis/缓存后台上报 > 无位置
