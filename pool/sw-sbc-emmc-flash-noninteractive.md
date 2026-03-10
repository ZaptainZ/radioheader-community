---
id: sw-sbc-emmc-flash-noninteractive
domain: SBC, Linux, DevOps
tags: eMMC 刷机 | armbian-install | dd | SSH 管道 | 非交互 | 嵌入式 | flash | 远程部署 | SBC | ARM
refs: topics/product-hardware.md
---
### 远程刷写 SBC eMMC：绕过交互式安装工具

symptoms: armbian-install 报 "TERM environment variable needs set"；SSH 远程无法操作交互式 TUI 工具
context: 通过 SSH 远程将系统从 SD 卡安装到 eMMC，没有物理显示器/键盘
cause: armbian-install / nand-sata-install 依赖 dialog TUI，需要完整终端环境，SSH 管道模式下不可用
fix: 用 SSH 管道直接 dd 写入 eMMC，然后手动扩展分区和文件系统：
  1. `cat image.img | ssh root@device 'dd of=/dev/mmcblkN bs=4M conv=fsync'`
  2. `sgdisk -e /dev/mmcblkN`（修复 GPT 到磁盘末尾）
  3. `sgdisk -d 1 -n 1:32768:0 -t 1:8305 /dev/mmcblkN`（删除重建分区填满空间）
  4. `partprobe && e2fsck -f -y /dev/mmcblkNp1 && resize2fs /dev/mmcblkNp1`
