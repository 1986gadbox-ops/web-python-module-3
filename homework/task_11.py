def compare_files(file1, file2):
    with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    max_len = max(len(lines1), len(lines2))
    mismatch_found = False

    for i in range(max_len):
        line1 = lines1[i].rstrip('n') if i < len(lines1) else None
        line2 = lines2[i].rstrip('n') if i < len(lines2) else None

        if line1 != line2:
            mismatch_found = True
            print(f"Несовпадающие строки на позиции {i+1}:")
            print(f"Файл 1: {line1 if line1 is not None else '<строка отсутствует>'}")
            print(f"Файл 2: {line2 if line2 is not None else '<строка отсутствует>'}")
            print()

    if not mismatch_found:
        print("Все строки совпадают.")

