---
id: sw-rust-plugin-permissions-manifest
domain: Rust, Plugin, Security, Serde
tags: 插件权限 | permissions | manifest.toml | 权限声明 | serde default | Option | 向后兼容 | backward compatible | network | filesystem | ipc_methods | 渐进式安全
refs: topics/rust-systems.md
---
### 插件权限声明的向后兼容设计

symptoms: 需要为插件系统增加权限声明，但不能破坏已有无权限段的 manifest 文件
context: TOML 格式的插件清单需要新增 `[permissions]` 段，旧插件没有这个段
cause: 直接加 required 字段会导致旧 manifest 解析失败
fix: 结构体用 `#[serde(default)]` + `Option<PluginPermissions>`，权限字段内部也各用 `#[serde(default)]`（bool 默认 false，Vec 默认空）。安装时仅用 `tracing::info!` 打印权限声明，不强制执行（渐进式安全：先声明后执行）。这样无 `[permissions]` 段的旧 manifest 反序列化得到 `None`，完全兼容
