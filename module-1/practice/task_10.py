# задание 1

# def print_users(codes, phones):
#     print("nСписок пользователей (код — телефон):")
#     for code, phone in zip(codes, phones):
#         print(f"{code} — {phone}")

# def sort_by_codes(codes, phones):
#     combined = list(zip(codes, phones))
#     combined.sort(key=lambda x: x[0])
#     codes_sorted, phones_sorted = zip(*combined)
#     return list(codes_sorted), list(phones_sorted)

# def sort_by_phones(codes, phones):
#     combined = list(zip(codes, phones))
#     combined.sort(key=lambda x: x[1])
#     codes_sorted, phones_sorted = zip(*combined)
#     return list(codes_sorted), list(phones_sorted)

# def main():
#     # Пример данных
#     codes = [102, 56, 77, 34, 89]
#     phones = [1234567, 9876543, 5550000, 3332222, 7778888]

#     while True:
#         print("Меню:")
#         print("1 - Отсортировать по идентификационным кодам")
#         print("2 - Отсортировать по номерам телефона")
#         print("3 - Вывести список пользователей")
#         print("0 - Выход")

#         choice = input("Выберите пункт меню: ").strip()

#         if choice == "1":
#             codes, phones = sort_by_codes(codes, phones)
#             print("Список отсортирован по идентификационным кодам.")
#         elif choice == "2":
#             codes, phones = sort_by_phones(codes, phones)
#             print("Список отсортирован по номерам телефона.")
#         elif choice == "3":
#             print_users(codes, phones)
#         elif choice == "0":
#             print("Выход из программы.")
#             break
#         else:
#             print("Некорректный выбор. Попробуйте снова.")

# if __name__ == "__main__":
#     main()



# задание 2



def print_books(titles, years):
    print("nСписок книг (название — год выпуска):")
    for title, year in zip(titles, years):
        print(f"{title} — {year}")

def sort_by_titles(titles, years):
    combined = list(zip(titles, years))
    combined.sort(key=lambda x: x[0].lower())
    titles_sorted, years_sorted = zip(*combined)
    return list(titles_sorted), list(years_sorted)

def sort_by_years(titles, years):
    combined = list(zip(titles, years))
    combined.sort(key=lambda x: x[1])
    titles_sorted, years_sorted = zip(*combined)
    return list(titles_sorted), list(years_sorted)

def main():
    titles = [
        "Война и мир",
        "Преступление и наказание",
        "Мастер и Маргарита",
        "Отцы и дети",
        "Анна Каренина"
    ]
    years = [1869, 1866, 1967, 1862, 1877]

    while True:
        print("Меню:")
        print("1 - Отсортировать по названию книг")
        print("2 - Отсортировать по году выпуска")
        print("3 - Вывести список книг")
        print("0 - Выход")

        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            titles, years = sort_by_titles(titles, years)
            print("Список отсортирован по названию книг.")
        elif choice == "2":
            titles, years = sort_by_years(titles, years)
            print("Список отсортирован по году выпуска.")
        elif choice == "3":
            print_books(titles, years)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()