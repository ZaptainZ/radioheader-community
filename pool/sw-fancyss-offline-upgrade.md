---
id: sw-fancyss-offline-upgrade
domain: Networking, Proxy, Merlin
tags: fancyss | 离线安装 | 升级 | offline install | koolshare | detect_package | tar.gz | ks_tar_install | 软件中心
refs: topics/networking-proxy.md
---
### fancyss 离线升级方法（SSH）

symptoms: 路由器无法直连 GitHub 下载更新，或软件中心在线更新失败
context: Merlin 路由器上的 koolshare fancyss 插件需要升级
fix:
1. 从 `hq450/fancyss_history_package` 仓库下载对应平台的 tar.gz（Mac 端下载）
2. `scp -O` 上传到路由器 `/tmp/`（Merlin 无 sftp-server，需 `-O` 用旧协议）
3. 绕过包名检测：`sed -i 's/\tdetect_package/\t# detect_package/g' /koolshare/scripts/ks_tar_install.sh`
4. 解压：`tar xzf xxx.tar.gz -C /tmp/`
5. 安装：`cd /tmp/shadowsocks && sh install.sh`
6. 安装脚本会自动停止旧版、复制文件、重启服务，dbus 配置保留
