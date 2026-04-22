# задание 1


# def compare_files(file1, file2):
#     with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
#         lines1 = f1.readlines()
#         lines2 = f2.readlines()

#     max_len = max(len(lines1), len(lines2))
#     mismatch_found = False

#     for i in range(max_len):
#         line1 = lines1[i].rstrip('n') if i < len(lines1) else None
#         line2 = lines2[i].rstrip('n') if i < len(lines2) else None

#         if line1 != line2:
#             mismatch_found = True
#             print(f"Несовпадающие строки на позиции {i+1}:")
#             print(f"Файл 1: {line1 if line1 is not None else '<строка отсутствует>'}")
#             print(f"Файл 2: {line2 if line2 is not None else '<строка отсутствует>'}")
#             print()

#     if not mismatch_found:
#         print("Все строки совпадают.")



# задание 2

        
# def file_statistics(input_file, output_file):
#     vowels = "аеёиоуыэюяaeiouAEIOU"
#     consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#     digits = "0123456789"

#     with open(input_file, encoding="utf-8") as f:
#         text = f.read()

#     num_chars = len(text)
#     num_lines = text.count('n') + 1 if text else 0
#     num_vowels = sum(ch in vowels for ch in text)
#     num_consonants = sum(ch in consonants for ch in text)
#     num_digits = sum(ch in digits for ch in text)

#     with open(output_file, "w", encoding="utf-8") as f:
#         f.write(f"Количество символов: {num_chars}n")
#         f.write(f"Количество строк: {num_lines}n")
#         f.write(f"Количество гласных букв: {num_vowels}n")
#         f.write(f"Количество согласных букв: {num_consonants}n")
#         f.write(f"Количество цифр: {num_digits}n")


# задание 3


# def remove_last_line(input_file, output_file):
#     with open(input_file, encoding="utf-8") as f:
#         lines = f.readlines()

#     if lines:
#         lines = lines[:-1]

#     with open(output_file, "w", encoding="utf-8") as f:
#         f.writelines(lines)



# задание 4

# def longest_line_length(input_file):
#     max_length = 0
#     with open(input_file, encoding="utf-8") as f:
#         for line in f:
#             length = len(line.rstrip('n'))
#             if length > max_length:
#                 max_length = length
#     print(f"Длина самой длинной строки: {max_length}")



# задание 5

# def count_word_occurrences(input_file, word):
#     count = 0
#     word_lower = word.lower()
#     with open(input_file, encoding="utf-8") as f:
#         for line in f:
#             words = line.lower().split()
#             count += words.count(word_lower)
#     print(f"Слово '{word}' встречается {count} раз(а).")




    # задание 6



    def find_and_replace(input_file, output_file, old_word, new_word):
    with open(input_file, encoding="utf-8") as f:
        text = f.read()

    new_text = text.replace(old_word, new_word)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(new_text)

    print(f"Все вхождения '{old_word}' заменены на '{new_word}' и записаны в файл {output_file}")







        
