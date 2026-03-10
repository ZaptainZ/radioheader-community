---
id: sw-backend-nginx-catchall-locations
domain: Backend, Nginx
tags: Nginx | catch-all | server block | 404 | Host | 回源 | location | default_server
refs: topics/backend-deploy.md
---
### Nginx catch-all server block 也需要配各 location

symptoms: 非目标 Host 头的请求回源返回 404
context: Nginx 配了 catch-all（default_server）server block 处理未匹配的 Host
cause: catch-all server block 中没有配置 location 路由，所有请求都落到默认处理（通常返回 404）
fix: catch-all server block 中也需要配置各 location，或显式返回 444/403 拒绝非目标 Host
