---
id: sw-backend-aws-china-cloudfront
domain: Backend, AWS, China
tags: AWS | CloudFront | 中国区 | ICP | IAM 证书 | ACM | 403 | SSL | S3 | 代理环境变量
refs: topics/backend-deploy.md
---
### AWS 中国区 CloudFront 配置：ICP + IAM 证书 + 代理清理

symptoms: CloudFront 返回 403 或 SSL 证书错误

**ICP 域名**: AWS 中国区 CloudFront 必须绑定已备案的 ICP 域名

**SSL 证书**: 必须上传到 IAM（路径 `/cloudfront/`），不能用 ACM（报 "not available in this region"）

**回源**: CloudFront 回源走 HTTP 80，所有公开路由必须同时配在端口 80 和 443

**S3 上传**: 上传前必须清除代理环境变量（`env -u http_proxy -u https_proxy`），否则卡住或失败
