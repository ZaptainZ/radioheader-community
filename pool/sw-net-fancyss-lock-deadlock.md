---
id: sw-net-fancyss-lock-deadlock
domain: Networking, fancyss, Router
tags: fancyss | 死锁 | deadlock | koolss.lock | ssconfig.sh | 进程 | 卡住 | 无法重启
refs: topics/networking-proxy.md
---
### fancyss 多个 ssconfig.sh 进程抢锁导致死锁

symptoms: fancyss 无法启动/停止/切换节点，操作卡住无响应
context: 路由器上运行 fancyss，多次快速操作或异常中断后
cause: 多个 `ssconfig.sh` 进程同时竞争 `/var/lock/koolss.lock` 文件锁
fix: `killall ssconfig.sh && rm -f /var/lock/koolss.lock` 后重启 fancyss
