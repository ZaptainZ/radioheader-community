---
id: sw-net-openclash-subscription-chicken-egg
domain: Networking, OpenClash, Proxy
tags: OpenClash | 订阅更新 | subscription | 代理失败 | 鸡生蛋 | chicken-egg | scp | 配置恢复
refs: topics/networking-proxy.md
---
### OpenClash 订阅更新走透明代理，代理故障时无法自更新

symptoms: 代理失效后订阅也无法更新，陷入死循环
context: OpenClash 通过透明代理运行，订阅更新请求也走代理
cause: 订阅更新依赖透明代理→代理配置来自订阅→形成鸡生蛋循环
fix: 从另一台能上网的设备下载订阅配置文件，通过 `scp` 传到路由器覆盖旧配置，然后重启 OpenClash
