---
id: sw-rust-hashmap-borrow-extract-pattern
domain: Rust, Borrow Checker, HashMap
tags: borrow conflict | get_mut | self method | 借用冲突 | cannot borrow self | mutable immutable | HashMap | 提取数据 | owned values | block scope
refs: topics/rust-systems.md
---
### HashMap get_mut + self.method() 借用冲突：块作用域提取 owned 数据

symptoms: `cannot borrow *self as immutable because it is also borrowed as mutably` — 在 `self.map.get_mut(key)` 后调用 `self.other_method()`
context: struct 持有 HashMap，某方法需要先从 map 取值再调用 self 的其他方法
cause: `get_mut()` 持有 `&mut self` 借用，同时调用 `self.method()` 需要 `&self` 或 `&mut self`，借用冲突
fix: 用块作用域 `let (a, b) = { let v = self.map.get_mut(k).unwrap(); (v.field.clone(), v.other.clone()) };` 提取为 owned 值，块结束后借用释放，再调用 `self.method(a, b)`，最后重新 `self.map.get_mut(k)` 写回结果
verified: 编译通过，适用于所有 HashMap 值需要与 self 方法交互的场景
