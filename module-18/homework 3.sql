ids = [102, 45, 78, 23]
phones = [89101234567, 89215554433, 89098887766, 89991112233]

def display_list(ids_list, phones_list):
    print("Список пользователей:")
    for id_code, phone in zip(ids_list, phones_list):
        print(f"ID: {id_code} - Телефон: {phone}")

while True:
    print("\n Меню:")
    print("1. Отсортировать по идентификационным кодам")
    print("2. Отсортировать по номерам телефонов")
    print("3. Вывести список")
    print("4. Выход")
    choice = input("Выберите действие: ")

    if choice == '1':
        combined = list(zip(ids, phones))
        combined.sort(key=lambda x: x[0])
        ids, phones = zip(*combined)
        print("Отсортировано по ID.")
    elif choice == '2':
        combined = list(zip(ids, phones))
        combined.sort(key=lambda x: x[1])
        ids, phones = zip(*combined)
        print("Отсортировано по номерам.")
    elif choice == '3':
        display_list(ids, phones)
    elif choice == '4':
        print("Выход...")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")

----------------------------------------

titles = ["Война и мир", "Преступление и наказание", "Мастер и Маргарита", "Три товарища"]
years = [1869, 1866, 1967, 1936]

def display_books(titles_list, years_list):
    print("Список книг:")
    for title, year in zip(titles_list, years_list):
        print(f"{title} ({year})")

while True:
    print("\n Меню:")
    print("1. Отсортировать по названию книг")
    print("2. Отсортировать по годам выпуска")
    print("3. Вывести список книг")
    print("4. Выход")
    choice = input("Выберите действие: ")

    if choice == '1':
        combined = list(zip(titles, years))
        combined.sort(key=lambda x: x[0])
        titles, years = zip(*combined)
        print("Отсортировано по названию.")
    elif choice == '2':
        combined = list(zip(titles, years))
        combined.sort(key=lambda x: x[1])
        titles, years = zip(*combined)
        print("Отсортировано по году.")
    elif choice == '3':
        display_books(titles, years)
    elif choice == '4':
        print("Выход...")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")