# def add_player(players, name, height):
#     if name in players:
#         print(f"Игрок с ФИО '{name}' уже существует.")
#     else:
#         players[name] = height
#         print(f"Игрок '{name}' добавлен с ростом {height} см.")

# def remove_player(players, name):
#     if name in players:
#         del players[name]
#         print(f"Игрок '{name}' удалён.")
#     else:
#         print(f"Игрок с ФИО '{name}' не найден.")

# def find_player(players, name):
#     if name in players:
#         print(f"Игрок '{name}' найден, рост: {players[name]} см.")
#     else:
#         print(f"Игрок с ФИО '{name}' не найден.")

# def replace_player(players, name, new_height):
#     if name in players:
#         players[name] = new_height
#         print(f"Рост игрока '{name}' обновлён на {new_height} см.")
#     else:
#         print(f"Игрок с ФИО '{name}' не найден.")

# def print_all(players):
#     if not players:
#         print("Список баскетболистов пуст.")
#     else:
#         print("Список баскетболистов:")
#         for name, height in players.items():
#             print(f"- {name}: {height} см")

# def main():
#     players = {}
#     while True:
#         print("nДоступные операции:")
#         print("1 - Добавить игрока")
#         print("2 - Удалить игрока")
#         print("3 - Найти игрока")
#         print("4 - Изменить рост игрока")
#         print("5 - Показать всех игроков")
#         print("0 - Выход")

#         choice = input("Выберите операцию: ").strip()

#         if choice == '1':
#             name = input("Введите ФИО игрока: ").strip()
#             height_str = input("Введите рост игрока (см): ").strip()
#             if height_str.isdigit():
#                 height = int(height_str)
#                 add_player(players, name, height)
#             else:
#                 print("Рост должен быть числом.")
#         elif choice == '2':
#             name = input("Введите ФИО игрока для удаления: ").strip()
#             remove_player(players, name)
#         elif choice == '3':
#             name = input("Введите ФИО игрока для поиска: ").strip()
#             find_player(players, name)
#         elif choice == '4':
#             name = input("Введите ФИО игрока для изменения роста: ").strip()
#             height_str = input("Введите новый рост (см): ").strip()
#             if height_str.isdigit():
#                 height = int(height_str)
#                 replace_player(players, name, height)
#             else:
#                 print("Рост должен быть числом.")
#         elif choice == '5':
#             print_all(players)
#         elif choice == '0':
#             print("Выход из программы.")
#             break
#         else:
#             print("Некорректный ввод. Попробуйте снова.")

# if __name__ == "__main__":
#     main()



# задание 2


# import json
# import os

# DICTIONARY_FILE = "eng_fr_dict.json"

# def load_dictionary(path=DICTIONARY_FILE):
#     if os.path.exists(path):
#         with open(path, "r", encoding="utf-8") as f:
#             try:
#                 data = json.load(f)
#                 if isinstance(data, dict):
#                     return data
#             except json.JSONDecodeError:
#                 pass
#     return {}

# def save_dictionary(d, path=DICTIONARY_FILE):
#     with open(path, "w", encoding="utf-8") as f:
#         json.dump(d, f, ensure_ascii=False, indent=2)

# def add_word(dictionary, english, french):
#     dictionary[english] = french
#     print(f"Добавлено: '{english}' -> '{french}'")

# def delete_word(dictionary, english):
#     if english in dictionary:
#         del dictionary[english]
#         print(f"Удалено: '{english}'")
#     else:
#         print(f"Слово '{english}' не найдено.")

# def search_word(dictionary, english):
#     if english in dictionary:
#         print(f"{english} -> {dictionary[english]}")
#         return dictionary[english]
#     else:
#         print(f"Слово '{english}' не найдено.")
#         return None

# def replace_word(dictionary, english, new_french):
#     if english in dictionary:
#         dictionary[english] = new_french
#         print(f"Заменено: '{english}' -> '{new_french}'")
#     else:
#         print(f"Слово '{english}' не найдено. Добавьте его вместо замены.")

# def list_all(dictionary):
#     if not dictionary:
#         print("Словарь пуст.")
#     else:
#         for eng, fr in dictionary.items():
#             print(f"{eng} : {fr}")

# def main():
#     dictionary = load_dictionary()

#     while True:
#         print("\nВыберите действие: ")
#         print("1. Добавить слово")
#         print("2. Удалить слово")
#         print("3. Найти перевод")
#         print("4. Заменить перевод")
#         print("5. Показать весь словарь")
#         print("6. Сохранить и выйти")
#         print("7. Выйти без сохранения")
#         choice = input("Введите номер пункта: ").strip()

#         if choice == "1":
#             eng = input("Введите английское слово: ").strip()
#             fr = input("Введите французский перевод: ").strip()
#             if eng and fr:
#                 add_word(dictionary, eng, fr)
#             else:
#                 print("Оба поля должны быть заполнены.")
#         elif choice == "2":
#             eng = input("Введите английское слово для удаления: ").strip()
#             if eng:
#                 delete_word(dictionary, eng)
#             else:
#                 print("Введите слово.")
#         elif choice == "3":
#             eng = input("Введите английское слово для поиска: ").strip()
#             if eng:
#                 search_word(dictionary, eng)
#             else:
#                 print("Введите слово.")
#         elif choice == "4":
#             eng = input("Введите английское слово: ").strip()
#             new_fr = input("Введите новый французский перевод: ").strip()
#             if eng and new_fr:
#                 replace_word(dictionary, eng, new_fr)
#             else:
#                 print("Оба поля должны быть заполнены.")
#         elif choice == "5":
#             list_all(dictionary)
#         elif choice == "6":
#             save_dictionary(dictionary)
#             print("Словарь сохранён. Выход.")
#             break
#         elif choice == "7":
#             print("Выход без сохранения.")
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")

# if __name__ == "__main__":
#     main()




# задание 3


# import json
# import os

# DATA_FILE = "firma_contacts.json"

# def load_contacts(path=DATA_FILE):
#     if os.path.exists(path):
#         with open(path, "r", encoding="utf-8") as f:
#             try:
#                 data = json.load(f)
#                 if isinstance(data, dict):
#                     return data
#             except json.JSONDecodeError:
#                 pass
#     return {}

# def save_contacts(contacts, path=DATA_FILE):
#     with open(path, "w", encoding="utf-8") as f:
#         json.dump(contacts, f, ensure_ascii=False, indent=2)

# def add_contact(contacts, id_key, details):
#     if id_key in contacts:
#         print(f"Контакт с идентификатором '{id_key}' уже существует. Замена данных не требуется — используйте замену.")
#         return False
#     contacts[id_key] = details
#     print(f"Добавлен контакт: {id_key}")
#     return True

# def delete_contact(contacts, id_key):
#     if id_key in contacts:
#         del contacts[id_key]
#         print(f"Удалён контакт: {id_key}")
#         return True
#     print(f"Контакт с идентификатором '{id_key}' не найден.")
#     return False

# def search_contact(contacts, id_key):
#     if id_key in contacts:
#         return id_key, contacts[id_key]
#     return None

# def replace_contact(contacts, id_key, field, new_value):
#     if id_key not in contacts:
#         print(f"Контакт с идентификатором '{id_key}' не найден.")
#         return False
#     if field not in contacts[id_key]:
#         print(f"Поле '{field}' не существует.")
#         return False
#     contacts[id_key][field] = new_value
#     print(f"Обновлено {field} для '{id_key}' -> {new_value}")
#     return True

# def list_contacts(contacts):
#     if not contacts:
#         print("Справочник пуст.")
#         return
#     for id_key, info in contacts.items():
#         print(f"ID: {id_key}")
#         for k, v in info.items():
#             print(f"  {k}: {v}")
#         print("-" * 20)

# def main():
#     contacts = load_contacts()

#     while True:
#         print("\nВыберите действие:")
#         print("1. Добавить контакт")
#         print("2. Удалить контакт")
#         print("3. Найти контакт")
#         print("4. Заменить данные контакта")
#         print("5. Показать все контакты")
#         print("6. Сохранить и выйти")
#         print("7. Выйти без сохранения")
#         choice = input("Введите номер пункта: ").strip()

#         if choice == "1":
#             id_key = input("Введите уникальный идентификатор контакта (например, ФИО или IntlID): ").strip()
#             fio = input("ФИО: ").strip()
#             phone = input("Телефон: ").strip()
#             email = input("Рабочий email: ").strip()
#             position = input("Должность: ").strip()
#             office = input("Номер кабинета: ").strip()
#             skype = input("Skype: ").strip()

#             details = {
#                 "ФИО": fio,
#                 "Телефон": phone,
#                 "Email": email,
#                 "Должность": position,
#                 "Кабинет": office,
#                 "Skype": skype
#             }
#             if id_key and any(details.values()):
#                 add_contact(contacts, id_key, details)
#             else:
#                 print("Заполните хотя бы одно поле и идентификатор.")
#         elif choice == "2":
#             id_key = input("Введите идентификатор контакта для удаления: ").strip()
#             if id_key:
#                 delete_contact(contacts, id_key)
#             else:
#                 print("Укажите идентификатор.")
#         elif choice == "3":
#             id_key = input("Введите идентификатор для поиска: ").strip()
#             if id_key:
#                 result = search_contact(contacts, id_key)
#                 if result:
#                     k, info = result
#                     print(f"Найдено: ID={k}")
#                     for fk, fv in info.items():
#                         print(f"  {fk}: {fv}")
#                 else:
#                     print("Контакт не найден.")
#             else:
#                 print("Укажите идентификатор.")
#         elif choice == "4":
#             id_key = input("Введите идентификатор контакта для замены данных: ").strip()
#             if not id_key:
#                 print("Укажите идентификатор.")
#                 continue
#             if id_key not in contacts:
#                 print(f"Контакт '{id_key}' не найден.")
#                 continue
#             print("Доступные поля: ФИО, Телефон, Email, Должность, Кабинет, Skype")
#             field = input("Какое поле заменить? ").strip()
#             new_value = input("Новое значение: ").strip()

#             field_map = {
#                 "ФИО": "ФИО",
#                 "ФИО ": "ФИО",
#                 "Телефон": "Телефон",
#                 "Email": "Email",
#                 "Должность": "Должность",
#                 "Кабинет": "Кабинет",
#                 "Skype": "Skype"
#             }

#             if field in field_map:
#                 pass
#             else:
#                 print("Неверное имя поля.")
#                 continue
#             replace_contact(contacts, id_key, field, new_value)
#         elif choice == "5":
#             list_contacts(contacts)
#         elif choice == "6":
#             save_contacts(contacts)
#             print("Справочник сохранён. Выход.")
#             break
#         elif choice == "7":
#             print("Выход без сохранения.")
#             break
#         else:
#             print("Некорректный выбор. Попробуйте снова.")

# if __name__ == "__main__":
#     main()








