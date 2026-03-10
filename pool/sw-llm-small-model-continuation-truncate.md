---
id: sw-llm-small-model-continuation-truncate
domain: LLM, Local Inference, Text Processing
tags: 小模型续写 | 假对话 | Human 截断 | User 截断 | 0.6B | 1B | continuation | hallucinated conversation | role marker | response extraction | 回复提取 | 模型输出清理
refs: topics/rust-systems.md
---
### 小参数本地模型回复中的假对话续写问题

symptoms: 本地小模型（≤1B）回复中出现 "Human:" "User:" 开头的假对话，看起来像模型自己在角色扮演多轮对话
context: 0.5B-1.8B 参数的本地 LLM 做单轮问答，max_tokens 够大时模型不停在生成
cause: 小模型缺乏对话终止的 EOS 能力，倾向于续写训练数据中的多轮对话模式
fix: 在提取回复文本后，扫描 `Human:`、`human:`、`User:`、`user:` 标记，首次命中位置之前截断。确保截断在 `idx > 0` 时才生效（避免空结果）
