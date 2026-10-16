import scripts.extract_all_2004_expls as mod

for q in [1, 2, 6, 10, 20]:
    print(f"==================== Q{q} ====================")
    print(mod.expl_map[q][:600])
