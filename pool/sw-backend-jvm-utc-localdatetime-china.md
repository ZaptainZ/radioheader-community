---
id: sw-backend-jvm-utc-localdatetime-china
domain: Java, Spring Boot, Backend
tags: 时区 | timezone | LocalDateTime.now() | ZoneId | UTC | Asia/Shanghai | 时间差8小时 | 时间不对 | system prompt 时间 | -Duser.timezone=UTC | 中国时间
refs: topics/backend-deploy.md
---
### JVM UTC 模式下 LocalDateTime.now() 返回 UTC 而非本地时间

symptoms: 应用显示的时间比实际时间早/晚 8 小时；system prompt 中注入的"当前时间"与用户体感不符（如晚上显示中午）
context: JVM 启动参数含 `-Duser.timezone=UTC`（常见于数据库一致性需求），但业务逻辑需要展示中国时间
fix: `LocalDateTime.now(ZoneId.of("Asia/Shanghai"))` 显式指定时区，不要用无参 `LocalDateTime.now()`
caveats:
- 数据库存储仍用 UTC，仅在展示/注入 prompt 时转换
- 同一项目中可能同时存在"存储用 UTC"和"显示用本地时间"两种需求，每处 `LocalDateTime.now()` 都要确认意图
