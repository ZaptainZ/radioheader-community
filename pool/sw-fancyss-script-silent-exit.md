---
id: sw-fancyss-script-silent-exit
domain: Networking, Proxy, Shell
tags: fancyss | ss_online_update | 订阅失败 | 无输出 | silent exit | 静默退出 | no output | 脚本参数 | case $2
refs: topics/networking-proxy.md
---
### fancyss 订阅更新脚本无输出静默退出

symptoms: 运行 `sh ss_online_update.sh 3` 无任何输出，订阅不更新，节点列表无变化
context: fancyss 路由器代理插件，通过脚本更新订阅节点
cause: 脚本内 `case $2 in` 匹配第二个参数。只传一个参数时 `$2` 为空，不匹配任何分支，直接退出
fix: 传两个参数：`sh ss_online_update.sh fancyss 3`（第一个参数会被赋给 ACTION/ID 但 case 匹配 $2）。查看 crontab 中的调用方式可确认正确参数格式
