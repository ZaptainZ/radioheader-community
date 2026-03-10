---
id: sw-backend-spring-async-enable
domain: Backend, Spring Boot, Java
tags: @Async | @EnableAsync | 异步不生效 | async not working | 同步执行 | 代理 | proxy | 同类调用
refs: topics/ai-api-integration.md
---
### Spring Boot @Async 方法不异步执行

symptoms: 标注了 `@Async` 的方法实际上同步执行，没有新线程
context: Spring Boot 项目中使用 `@Async` 注解
cause: 缺少 `@EnableAsync` 注解，或者在同一个类内部调用 @Async 方法（不走 Spring 代理）
fix:
- Application 类加 `@EnableAsync`
- `@Async` 方法必须是 public 且被**外部**类调用（自调用不走代理，不会异步）
