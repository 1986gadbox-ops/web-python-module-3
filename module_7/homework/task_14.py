import json

class Employee:
    def __init__(self, first_name, last_name, age, position):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'position': self.position
        }

    @staticmethod
    def from_dict(data):
        return Employee(
            data['first_name'],
            data['last_name'],
            data['age'],
            data['position']
        )

def load_employees(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Employee.from_dict(emp) for emp in data]
    except FileNotFoundError:
        print("Файл не найден. Загружается пустой список сотрудников.")
        return []

def save_employees(filename, employees):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([emp.to_dict() for emp in employees], f, ensure_ascii=False, indent=4)

def add_employee(employees):
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    age = int(input("Введите возраст: "))
    position = input("Введите должность: ")
    employees.append(Employee(first_name, last_name, age, position))
    print("Сотрудник добавлен.")

def edit_employee(employees):
    last_name = input("Введите фамилию сотрудника, которого хотите редактировать: ")
    for emp in employees:
        if emp.last_name == last_name:
            print(f"Редактирование сотрудника: {emp.first_name} {emp.last_name}")
            emp.first_name = input("Введите новое имя: ") or emp.first_name
            emp.last_name = input("Введите новую фамилию: ") or emp.last_name
            age_input = input("Введите новый возраст: ")
            if age_input:
                emp.age = int(age_input)
            emp.position = input("Введите новую должность: ") or emp.position
            print("Информация обновлена.")
            return
    print("Сотрудник с такой фамилией не найден.")

def delete_employee(employees):
    last_name = input("Введите фамилию сотрудника, которого хотите удалить: ")
    for i, emp in enumerate(employees):
        if emp.last_name == last_name:
            del employees[i]
            print("Сотрудник удален.")
            return
    print("Сотрудник с такой фамилией не найден.")

def search_by_last_name(employees):
    last_name = input("Введите фамилию для поиска: ")
    result = [emp for emp in employees if emp.last_name == last_name]
    if result:
        for emp in result:
            print_employee(emp)
    else:
        print("Сотрудник(и) не найден(ы).")

def search_by_age(employees):
    age = int(input("Введите возраст для поиска: "))
    result = [emp for emp in employees if emp.age == age]
    if result:
        for emp in result:
            print_employee(emp)
    else:
        print("Сотрудник(и) не найден(ы).")

def search_by_letter(employees):
    letter = input("Введите первую букву фамилии: ").lower()
    result = [emp for emp in employees if emp.last_name.lower().startswith(letter)]
    if result:
        for emp in result:
            print_employee(emp)
    else:
        print("Сотрудников, начинающихся на эту букву, не найдено.")

def print_employee(emp):
    print(f"Имя: {emp.first_name}, Фамилия: {emp.last_name}, Возраст: {emp.age}, Должность: {emp.position}")

def show_all_employees(employees):
    if not employees:
        print("Список сотрудников пуст.")
    else:
        for emp in employees:
            print_employee(emp)

def main():
    filename = input("Введите имя файла для загрузки данных: ")
    employees = load_employees(filename)

    while True:
        print("Выберите действие:")
        print("1. Добавить сотрудника")
        print("2. Редактировать сотрудника")
        print("3. Удалить сотрудника")
        print("4. Поиск по фамилии")
        print("5. Поиск по возрасту")
        print("6. Поиск по первой букве фамилии")
        print("7. Вывести всех сотрудников")
        print("8. Сохранить текущий список в файл")
        print("9. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            edit_employee(employees)
        elif choice == '3':
            delete_employee(employees)
        elif choice == '4':
            search_by_last_name(employees)
        elif choice == '5':
            search_by_age(employees)
        elif choice == '6':
            search_by_letter(employees)
        elif choice == '7':
            show_all_employees(employees)
        elif choice == '8':
            save_employees(filename, employees)
            print("Данные сохранены.")
        elif choice == '9':
            save_employees(filename, employees)
            print("Данные сохранены. Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()