---
id: sw-linux-gpt-resize-sgdisk
domain: Linux, Storage
tags: GPT | 分区扩展 | sgdisk | parted | resize | growpart | 非交互 | partition | Fix/Ignore
refs: topics/product-hardware.md
---
### GPT 分区非交互扩展用 sgdisk，不用 parted

symptoms: parted resizepart 卡在 "Fix/Ignore?" 提示；growpart 未安装
context: 将小镜像 dd 到大磁盘后，需要扩展分区到全部可用空间
cause: parted 检测到 GPT 备份表不在磁盘末尾时弹交互提示，脚本模式下会卡死
fix: 用 sgdisk（gdisk 包）替代：
  1. `sgdisk -e /dev/sdX`（移动备份 GPT 到磁盘末尾，非交互）
  2. `sgdisk -d 1 -n 1:原起始扇区:0 -t 1:8305 /dev/sdX`（删除重建，0 = 用到末尾）
  3. `partprobe && resize2fs /dev/sdX1`
