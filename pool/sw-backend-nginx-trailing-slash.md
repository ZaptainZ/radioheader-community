---
id: sw-backend-nginx-trailing-slash
domain: Backend, Nginx, Reverse Proxy
tags: proxy_pass | 末尾斜杠 | trailing slash | 路径丢失 | path strip | location 前缀 | 404 | API 路由
refs: topics/backend-deploy.md
---
### Nginx proxy_pass 末尾斜杠会剥离 location 前缀

symptoms: 反向代理后后端收到的路径缺少前缀（如 `/api` 丢失），导致 404
context: Nginx `location /api { proxy_pass http://backend/; }` 配置
cause: `proxy_pass` URI 末尾有 `/` 时，Nginx 将 location 匹配部分替换而非拼接。`/api/users` → 后端收到 `/users`
fix: 去掉末尾斜杠 `proxy_pass http://backend;`（保持原始路径），或后端路由适配无前缀路径
