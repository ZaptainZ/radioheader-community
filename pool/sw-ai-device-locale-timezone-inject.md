---
id: sw-ai-device-locale-timezone-inject
domain: AI, Prompt Engineering, i18n
tags: locale | timezone | 语言 | 繁体中文 | 回复语言错误 | system prompt | 设备信息 | Locale.current | TimeZone.current | 本地化
refs: topics/ai-api-integration.md
---
### 设备 locale/timezone 注入 system prompt 控制回复语言

symptoms: AI 清除历史后首次对话用错误语言回复（如简体中文用户收到繁体中文）

**根因**: 无历史对话时 LLM 无法推断用户语言，默认行为不可控。

**解决**: 客户端每次请求附带设备语言和时区（如 `zh_CN`、`Asia/Shanghai`），后端注入 system prompt：
```
用户终端语言：zh_CN（请使用此语言回复用户，除非用户明确要求使用其他语言）
```

**时间本地化**: 用客户端 timezone 计算当前时间（`LocalDateTime.now(ZoneId.of(timezone))`），而非服务器时区，确保"现在几点"等问题回答正确。
