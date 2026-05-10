class SupportRequest:
    def __init__(self, number: int, employee_name: str, description: str):
        self.number = number
        self.employee_name = employee_name
        self.description = description
        self.status = 'новая'

    def __str__(self):
        return(f"номер: {self.number}\n"
               f"сотрудник: {self.employee_name}\n"
               f"проблема: {self.description}\n"
               f"статус: {self.status}\n")

class RequestManager:
    def __init__(self):
        self._requests = []
        self._next_number = 1

    def add_request(self, employee_name: str, description: str):
        request = SupportRequest(self._next_number, employee_name, description)
        self._requests.append(request)
        self._next_number += 1

    def get_all_requests(self):
        return self._requests

    def find_requests_by_employee(self, employee_name: str):
        return [req for req in self._requests if req.employee_name.lower() == employee_name.lower()]

    def get_open_requests(self):
        return [req for req in self._requests if req.status in ["новая", "в работе"]]

    def get_request_by_number(self, number: int):
        for req in self._requests:
            if req.number == number:
                return req
        return None

    def change_request_status(self, number: int, new_status: str):
        request = self.get_request_by_number(number)
        if request and new_status in ["новая", "в заботе", "закрыта"]:
            request_status = new_status
            return True
        return False

class ConsoleMenu:
    def __init__(self, manager: RequestManager):
        self.manager = manager

    def show_menu(self):
        print("Меню")
        print("1. Добавить заявку")
        print("2. Показать все заявки")
        print("3. Изменить статус заявки")
        print("4. Показать открытые заявки")
        print("5. Найти заявки по имени сотрудника")
        print("0. Выход")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Выберите пункт меню: ")
            if choice == "1":
                self.add_request()
            elif choice =="2":
                self.show_all_requests()
            elif choice == "3":
                self.change_request_status()
            elif choice == "4":
                self.show_open_requests()
            elif choice == "5":
                self.find_requests_by_employee()
            elif choice == "0":
                print("Выход из программы.")
                break
            else:
                print("Некорректный выборю")

    def add_request(self):
        employee_name = input("Введите имя сотрудника: ")
        description = input("Описание проблемы: ")
        self.manager.add_request(employee_name, description)
        print("Заявка добавлена.")

    def show_all_requests(self):
        requests = self.manager.get_all_requests()
        if not requests:
            print("Нет заявок.")
        for req in requests:
            print(req)

    def change_request_status(self):
        try:
            number = int(input("Введите номер заявки: "))
            request = self.manager.get_request_by_number(number)
            if not request:
                print("Заявка не найдена.")
                return
            print(f"Текущий статус: {request.status}")
            new_status = input("Введите новый статус (новая, в работе, закрыта): ").lower()
            if new_status not in ["новая", "в работе", "закрыта"]:
                print("Некорректный статус.")
                return
            self.manager.change_request_status(number, new_status)
            print("Статус обновлён.")
        except ValueError:
            print("Некорректный ввод номера заявки.")

    def show_open_requests(self):
        requests = self.manager.get_open_requests()
        if not requests:
            print("Нет открытых заявок.")
        for req in requests:
            print(req)

    def find_requests_by_employee(self):
        employee_name = input("Введите имя сотрудника: ")
        requests = self.manager.find_requests_by_employee(employee_name)
        if not requests:
            print("Заявки не найдены.")
        for req in requests:
            print(req)

if __name__ == "__main__":
    manager = RequestManager()
    menu = ConsoleMenu(manager)
    menu.run()
