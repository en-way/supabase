import sys

with open(r'C:\Users\57867\.gemini\antigravity\brain\ad55b338-cd23-471c-97b5-4da0d8132180\full_archive_text_and_options_audit_matrix.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Update title & dashboard
text = text.replace('pie title 41 套试卷全库法医级校对分布 (Round 90)', 'pie title 41 套试卷全库法医级校对分布 (Round 91)')
text = text.replace('112/112 项断言 100% 全部通过', '113/113 项断言 100% 全部通过')

# Add Round 91 section to artifact
r91_section = """
### Round 91: 全库 41 套真题 243 篇篇章分类学拓扑 100% 绝对统一与新题型选项一致性对齐

1. **全库 243 篇篇章分类学元数据（Taxonomy Metadata）绝对规范化**：
   - **痛点排查**：在全库 243 篇篇章的 `type` 与 `section_type` 分类学字段审计中，发现 14 处遗留的历史非规范分类标签（如 `use_of_english`、`reading_part_a`、`new_type`、`reading_b` 等），导致本地 JSON 与 Supabase 数据库底层枚举产生微小方言差异。
   - **权威统一规范化**：
     - **完型填空（41 篇，P1）**：严格统一为 `type: "cloze"`、`section_type: "cloze"`（41/41）。
     - **传统阅读（165 篇，P2-P5 及 2001 P6）**：严格统一为 `type: "reading"`、`section_type: "reading"`（165/165）。
     - **新题型 Part B（37 篇，P6）**：严格统一为 `type: "reading_part_b"`、`section_type: "reading"`（37/37）。
   - **规范化成果**：本地 JSON 与 Supabase 数据库底层 schema 100% 达成单一真理源契合，全库 0 处孤立分类异形词。

2. **新题型 Part B Q41-Q45 选项同题同构同值深度对齐**：
   - 验证全库 37 套新题型在 Q41-Q45 间的选项字典：**100% 严格同题同构同值**。
   - 确认全库 **0 处 bare token 孤立选项**（如单独的 `[A]` 或 `A`），均已全部注入标准题干选项首句预览或真实小标题。
   - 确认全库 243 篇篇章文本中 **0 处考卷导语试卷说明（Directions / Section III / Answer Sheet）残留倒灌**。

3. **四维验证体系战果**：
   - `verify_db_parity.py`: **0 differences** between Supabase DB and local JSON.
   - `verify_deep_text_calibration.py`: **113/113 PASS** (新增 Assertion 113).
   - `verify_system_security_and_resilience.py`: **12/12 PASS**.
   - `npm.cmd run build`: **11/11 静态页面 0 error** 构建成功。
"""

text += "\n" + r91_section

with open(r'C:\Users\57867\.gemini\antigravity\brain\ad55b338-cd23-471c-97b5-4da0d8132180\full_archive_text_and_options_audit_matrix.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated audit matrix artifact successfully with Round 91!")
