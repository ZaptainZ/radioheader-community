---
id: sw-backend-enablewebmvc-disables-static
domain: Backend, Spring Boot
tags: @EnableWebMvc | 静态资源 | static resources | 404 | css | js | Spring Boot | 自动配置失效
refs: topics/backend-deploy.md
---
### @EnableWebMvc 会禁用 Spring Boot 默认静态资源服务

symptoms: `/css/**`、`/js/**` 等静态资源路径返回 404
context: Spring Boot 项目添加了 `@EnableWebMvc` 注解
cause: `@EnableWebMvc` 完全接管 MVC 配置，禁用 Spring Boot 的自动配置（包括默认静态资源映射）
fix: 移除 `@EnableWebMvc`（通常不需要），或显式注册静态资源路径，或由 Nginx 直接提供静态文件
