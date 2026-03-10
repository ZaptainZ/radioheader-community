---
id: sw-rust-sqlite-vec-auto-extension
domain: Rust, SQLite, Vector Search
tags: sqlite-vec | vec0 | 向量搜索 | KNN | sqlite3_auto_extension | rusqlite | 语义搜索 | embedding | cosine | 初始化顺序
refs: topics/rust-systems.md
---
### sqlite-vec 扩展必须在 Connection::open() 之前通过 auto_extension 注册

symptoms: vec0 虚拟表创建失败 "no such module: vec0"，或 sqlite-vec 功能不生效
context: Rust 项目用 rusqlite (bundled) + sqlite-vec crate 做向量搜索
cause: sqlite-vec 是 C 扩展，通过 `sqlite3_auto_extension` 注册后才在后续新连接中生效。如果先 open 再注册，当前连接不含扩展
fix: |
  ```rust
  unsafe {
      rusqlite::ffi::sqlite3_auto_extension(Some(std::mem::transmute(
          sqlite_vec::sqlite3_vec_init as *const ()
      )));
  }
  let conn = Connection::open(db_path)?; // 必须在注册之后
  ```
  sqlite-vec crate 不依赖特定 rusqlite 版本（纯 C FFI），rusqlite 0.31 bundled 可直接搭配
