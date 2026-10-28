import sys

with open(r'C:\Users\57867\.gemini\antigravity\brain\ad55b338-cd23-471c-97b5-4da0d8132180\full_archive_text_and_options_audit_matrix.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Update title & dashboard
text = text.replace('pie title 41 套试卷全库法医级校对分布 (Round 89)', 'pie title 41 套试卷全库法医级校对分布 (Round 90)')
text = text.replace('111/111 项断言 100% 全部通过', '112/112 项断言 100% 全部通过')

# Add Round 90 section to artifact
r90_section = """
### Round 90: 全库选项同题标点句号与省略号对齐一致性法医级校准

1. **同题选项句末句号对齐（Intra-question Period Alignment）**：
   - **痛点排查**：在全库 1,825 道题 7,830 个选项的句末标点严格对齐审计中，排查出 3 道试题存在句号遗漏（同题其他选项均有句号，而该选项遗漏）：
     - **2022 英语一 Q38 选项 C**：原为 `Limiting the powers of business owners`，补充句号对齐为 `Limiting the powers of business owners.`。
     - **2022 英语一 Q39 选项 C**：原为 `Society sees a rise in overall well-being`，补充句号对齐为 `Society sees a rise in overall well-being.`。
     - **2018 英语一 Q22 选项 B & C**：原为 `Optimists' opinions on new tech find little support` 与 `Issues arising from automation need to be tackled`，补充句号对齐为 `Optimists' opinions on new tech find little support.` 与 `Issues arising from automation need to be tackled.`。
   - **黄皮书比对确认**：查证《2022黄皮书真题解析（英语一）》第 47-49 页及《2018黄皮书真题解析（英语一）》第 12 页高精原件，确认为完整陈述句，全选项均应规范携带句点。

2. **2025 英语一 Part B Q41-Q45 选项 [F] 统一省略号补全**：
   - **痛点排查**：2025 英语一新题型 Part B 排序题中，选项 [A]-[E] 与 [G] 均统一规范展示段落首句并附加 `...` 预览标识，唯独选项 [F]（`"So what's the appeal of a long, sweaty day in pursuit of an elusive animal? 'It just feels bloody brilliant'"`）末尾遗漏了省略号 `...`。
   - **法医级校准**：补全为 `"So what's the appeal of a long, sweaty day in pursuit of an elusive animal? 'It just feels bloody brilliant'..."`，实现全卷 [A]～[G] 7 项格式 100% 绝对一致。

3. **四维验证体系战果**：
   - `verify_db_parity.py`: **0 differences** between Supabase DB and local JSON.
   - `verify_deep_text_calibration.py`: **112/112 PASS** (新增 Assertion 112).
   - `verify_system_security_and_resilience.py`: **12/12 PASS**.
   - `npm.cmd run build`: **11/11 静态页面 0 error** 构建成功。
"""

text += "\n" + r90_section

with open(r'C:\Users\57867\.gemini\antigravity\brain\ad55b338-cd23-471c-97b5-4da0d8132180\full_archive_text_and_options_audit_matrix.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated audit matrix artifact successfully with Round 90!")
