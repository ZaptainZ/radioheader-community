---
id: sw-fancyss-node-switch-stale-server
domain: Networking, Proxy
tags: fancyss | 切换节点 | ss_basic_server | v2ray.json | 节点不生效 | 旧服务器 | dbus | xray
refs: topics/networking-proxy.md
---
### fancyss 切换节点后代理仍连旧服务器

symptoms: 在 dbus 设了新的 `ssconf_basic_node` 并重启，但 xray 配置文件中 address 仍是旧节点的服务器
context: fancyss 旧版本（如 1.9.8），通过 SSH 切换节点后重启
cause: `ss_base.sh` 只将节点配置 export 为环境变量，不更新 dbus 中的 `ss_basic_server`。v2ray.json 生成代码可能读取 dbus 持久值而非环境变量
fix: 切换节点后手动同步：`dbus set ss_basic_server=新地址` + `sed -i` 修改 v2ray.json + 重启 xray。或通过 Web UI 切换（Web UI 会正确同步所有值）
