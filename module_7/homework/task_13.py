import json

class Employee:
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_dict(self):
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'age': self.age
        }

    @staticmethod
    def from_dict(data):
        return Employee(data['last_name'], data['first_name'], data['age'])

class EmployeeSystem:
    def __init__(self, filename):
        self.filename = filename
        self.employees = []
        self.load_employees()

    def load_employees(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.employees = [Employee.from_dict(emp) for emp in data]
        except FileNotFoundError:
            pass

    def save_employees(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            data = [emp.to_dict() for emp in self.employees]
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_employee(self, last_name, first_name, age):
        self.employees.append(Employee(last_name, first_name, age))

    def edit_employee(self, index, last_name, first_name, age):
        self.employees[index].last_name = last_name
        self.employees[index].first_name = first_name
        self.employees[index].age = age

    def delete_employee(self, index):
        del self.employees[index]

    def find_employees_by_last_name(self, last_name):
        return [emp for emp in self.employees if emp.last_name == last_name]

    def find_employees_by_age(self, age):
        return [emp for emp in self.employees if emp.age == age]

    def find_employees_by_initial(self, initial):
        return [emp for emp in self.employees if emp.last_name.startswith(initial)]

    def display_employees(self, employees):
        for emp in employees:
            print(f"{emp.last_name} {emp.first_name}, Возраст: {emp.age}")

def main():
    filename = input("Введите имя файла для сохранения данных: ")
    system = EmployeeSystem(filename)

    while True:
        print("\n1. Добавить сотрудника")
        print("2. Редактировать сотрудника")
        print("3. Удалить сотрудника")
        print("4. Поиск сотрудника по фамилии")
        print("5. Вывод сотрудников по возрасту")
        print("6. Вывод сотрудников по первой букве фамилии")
        print("7. Сохранить данные")
        print("8. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            age = int(input("Введите возраст: "))
            system.add_employee(last_name, first_name, age)

        elif choice == '2':
            index = int(input("Введите индекс сотрудника для редактирования: "))
            if 0 <= index < len(system.employees):
                last_name = input("Введите новую фамилию: ")
                first_name = input("Введите новое имя: ")
                age = int(input("Введите новый возраст: "))
                system.edit_employee(index, last_name, first_name, age)

        elif choice == '3':
            index = int(input("Введите индекс сотрудника для удаления: "))
            if 0 <= index < len(system.employees):
                system.delete_employee(index)

        elif choice == '4':
            last_name = input("Введите фамилию для поиска: ")
            results = system.find_employees_by_last_name(last_name)
            system.display_employees(results)

        elif choice == '5':
            age = int(input("Введите возраст для поиска: "))
            results = system.find_employees_by_age(age)
            system.display_employees(results)

        elif choice == '6':
            initial = input("Введите первую букву фамилии: ")
            results = system.find_employees_by_initial(initial)
            system.display_employees(results)

        elif choice == '7':
            system.save_employees()
            print("Данные сохранены.")

        elif choice == '8':
            system.save_employees()
            print("Выход из программы.")
            break

if __name__ == "__main__":
    main()