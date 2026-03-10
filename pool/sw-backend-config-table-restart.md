---
id: sw-backend-config-table-restart
domain: Backend, Spring Boot
tags: 配置表 | 缓存 | 重启 | 改表不生效 | config cache | 内存缓存 | restart required
refs: topics/backend-deploy.md
---
### 配置表启动时加载到内存缓存，改表后必须重启服务

symptoms: 修改数据库配置表后应用行为不变
context: Spring Boot 应用启动时将配置表数据加载到内存 Map/缓存
cause: 配置在启动时一次性加载，运行期间不重新读取数据库
fix: 修改配置表后必须重启服务。或实现配置热加载机制（如定时刷新、暴露 refresh 端点）
