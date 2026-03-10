---
id: sw-backend-mybatisplus-pagination-sort-order
domain: Backend, Java, MyBatis-Plus, MySQL
tags: 排序错乱 | 分页排序 | orderByDesc | 二级排序 | 同一秒 | 聊天记录顺序 | pagination sort | unstable sort | createdAt 相同 | 时间戳精度
refs: topics/backend-deploy.md
---
### MyBatis-Plus 分页查询只按 createdAt 排序，同秒记录顺序不确定

symptoms: 分页加载历史消息后，问答对顺序错乱（用户消息跑到 AI 回复前面或后面）；低频操作正常，快速连续操作时复现
context: 分页查询用 `orderByDesc(createdAt)`，createdAt 为 `datetime`（秒级精度），同一业务动作中连续 INSERT 的多条记录 createdAt 相同
cause: MySQL 对相同排序键的记录返回顺序不确定（unstable sort），分页后客户端 reverse 放大了错位
fix: 追加自增主键作为二级排序 `.orderByDesc(id)`，保证同秒记录按插入顺序排列
note: 任何有因果关系的成对记录（请求/响应、问/答、操作/日志）都需要二级排序
