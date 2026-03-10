---
id: sw-rust-aes-gcm-device-key-derivation
domain: Rust, Security, Encryption, Config
tags: AES-256-GCM | aes-gcm | API Key 加密 | 密钥派生 | machine-id | 设备指纹 | SHA-256 | salt | enc: 前缀 | 向后兼容 | 明文迁移 | config 加密 | key encryption at rest
refs: topics/rust-systems.md
---
### 用设备指纹派生密钥实现 API Key 加密存储

symptoms: 配置文件中 API Key 明文存储，存在泄漏风险
context: 嵌入式/桌面应用需要在本地配置文件中安全存储 API Key，无 KMS 可用
cause: 直接写明文到 TOML/JSON 配置文件
fix: 使用 `aes-gcm` 0.10 (AES-256-GCM)。密钥从设备指纹派生：读 `/etc/machine-id`（Linux）或 `hostname`（macOS fallback）→ SHA-256 + 固定 salt → 32 字节密钥。存储格式 `enc:base64(nonce12bytes + ciphertext)`。load 时检测 `enc:` 前缀自动解密，无前缀视为明文（向后兼容），save 时自动加密。空字符串不处理直接返回
