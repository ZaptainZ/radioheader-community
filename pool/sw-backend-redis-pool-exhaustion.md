---
id: sw-backend-redis-pool-exhaustion
domain: Backend, Java, Redis
tags: 401 | 间歇性失败 | intermittent | connection pool | 连接池耗尽 | 高并发 | Jedis | timeout
refs: topics/backend-deploy.md
---
### Redis 连接池默认值过小，高并发下耗尽导致间歇性 401

symptoms: 高并发时随机出现 401 未授权，低流量正常，重启暂时恢复
context: Spring Boot + Jedis 连接池，JWT Token 存储在 Redis 中
cause: Jedis 默认 max-active=8，并发请求超过 8 时无法获取连接，Token 查询失败 → 返回 401
fix: 配置 `spring.redis.jedis.pool.max-active=20`（或更高，按并发量调整）
note: 症状是 401 而非连接错误，容易误判为认证逻辑 bug
