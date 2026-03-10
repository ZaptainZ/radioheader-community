---
id: sw-sbc-remote-deploy-tips
domain: Hardware, SBC, Deployment
tags: SBC | 远程部署 | SSH | sudo | 密码 | xz | macOS | Python lzma | 脚本
refs: topics/product-hardware.md
---
### SBC 远程部署技巧：SSH 密码、xz 解压、手动脚本

symptoms: 远程操作 SBC 时遇到权限、工具缺失等障碍
context: 通过 SSH 远程管理 ARM SBC

**sudo 密码**: SSH 远程无法输入 sudo 密码时，创建脚本让用户在本地终端手动执行

**macOS 无 xz**: macOS 没有自带 xz 命令时，可用 Python `lzma` 模块解压 .xz 文件：`python3 -c "import lzma; open('out','wb').write(lzma.open('file.xz').read())"`
