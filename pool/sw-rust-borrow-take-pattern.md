---
id: sw-rust-borrow-take-pattern
domain: Rust, Ownership
tags: Rust | 借用冲突 | borrow | take | Option | 可变引用 | 不可变引用 | self | 同时借用
refs: topics/rust-systems.md
---
### Rust self 多字段同时借用冲突的 take/extract 模式

symptoms: 编译报 "cannot borrow `self` as mutable because it is also borrowed as immutable"
context: 需要同时可变访问 self 的一个字段 + 调用 self 的方法（隐式借用整个 self）

**Option take 模式**: `self.ai` 和 `self.players` 不能同时可变+不可变借用 → `let ai = self.ai.take()` → 操作 ai 和 self.players → `self.ai = Some(ai)`

**块作用域 extract 模式**: `self.map.get_mut(key)` + `self.method()` 冲突时，用 `{ let data = map.get(key).clone(); }` 块作用域提取 owned 数据释放借用 → 调方法 → 重新 `get_mut` 写回
