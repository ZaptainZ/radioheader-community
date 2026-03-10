---
id: sw-backend-redis-jwt-rdb-only
domain: Backend, Redis, Auth
tags: Redis | JWT | Token | 过期 | TTL | RDB | AOF | 重启丢失 | 401 | 登录失效
refs: topics/backend-deploy.md
---
### JWT 无 exp 靠 Redis TTL 管理过期，仅 RDB 快照时重启会丢 Token

symptoms: Redis 重启后用户大规模登录失效（401），需重新登录
context: JWT 不含 `exp` 字段，过期完全由 Redis key TTL 控制，Redis 只开了 RDB 快照（无 AOF）
cause: RDB 快照有时间间隔，重启时最近写入的 key（含有效 Token）丢失
fix: 开启 AOF 持久化（`appendonly yes`），或在 JWT 中设 `exp` 字段做双重过期保障
