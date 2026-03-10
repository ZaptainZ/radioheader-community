---
id: sw-sqlite-fts5-unicode61-cjk-substring
domain: SQLite, FTS5, CJK, 中文搜索
tags: FTS5 | unicode61 | 中文搜索 | 子串匹配 | MATCH 无结果 | tokenizer | CJK | LIKE | 全文检索 | 搜索不到 | 0 results | chinese search
refs: topics/rust-systems.md
---
### SQLite FTS5 unicode61 tokenizer 不支持中文子串搜索

symptoms: FTS5 MATCH 查询中文子串（如搜"火锅"匹配"我喜欢吃火锅"）返回 0 结果
context: 使用 `tokenize='unicode61'` 的 FTS5 虚拟表存储中文文本
cause: unicode61 按 Unicode 类别分词，连续 CJK 字符被视为一个完整 token。搜索 "火锅" 不会匹配包含 "我喜欢吃火锅" 的 token，因为整段是一个 token
fix: 小数据量场景用 `LIKE '%query%'` 替代 FTS5 MATCH。FTS5 表可保留供未来升级（如 sqlite-vec 语义搜索或接入分词器）
note: `datetime('now','localtime')` 精度只到秒，同毫秒插入的记录 ORDER BY created_at 不可靠，需改用 ORDER BY id（AUTOINCREMENT 单调递增）
