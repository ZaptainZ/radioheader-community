---
id: sw-backend-systemd-envfile-export
domain: Backend, Linux, systemd
tags: EnvironmentFile | export | 环境变量加载失败 | 变量为空 | KEY=VALUE | systemd service | .env | 配置不生效 | silent failure
refs: topics/backend-deploy.md
---
### systemd EnvironmentFile 不支持 export 前缀

symptoms: 服务启动后环境变量为空，`@Value("${KEY}")` 注入空字符串，功能静默失效（无报错）
context: systemd service 使用 `EnvironmentFile=/path/.env` 加载环境变量
cause: systemd 的 EnvironmentFile 解析器只接受 `KEY=VALUE` 格式，写成 `export KEY=VALUE` 会导致整行被忽略，且无错误日志
fix: `.env` 文件中不加 `export` 前缀，只写 `KEY=VALUE`；注意 `source .env` 和 systemd EnvironmentFile 格式互不兼容
