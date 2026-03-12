# def devide(a, b):
#     return a / b

# # print(devide(10, 0))

# raw_velues = ["10", "5", "abc", "3"]
# numbers = []

# for raw in raw_values:
#     try:
#         nambers.append(int(raw))
#     except ValueError:
#         print(f"Не число {raw}")

# print(nambers)


# def parse(a, b):
#     try:
#         x = int(a)
#         Y = int(b)
#     except ValueError:
#         return "Ошибка а или b не число"
#     except ZeroDivisionError:
#         return "Делить на ноль нельзя"

# print(parse("10", "2"))
# print(parse("10", "0"))
# print(parse("abc", "2"))


# try:
#     data = {"name": "Alice"}
#     print(data["email"])
# except KeyError as e:
#     print("Тип:", type(e).__name__)
#     print("Аргумент:", e.args)
#     print("Сообщение:", e)


# def set_discount(percent):
#     if not 0 <= percent <= 100:
#         raise ValueError("Скидка должна быть в деапазоне от 0 до 100.")
#     return f"Скидка установленна: {percent}%"

# print(set_discount(20))
# print(set_discount(120))



# def load_user(data user_id):
#     try:
#         return data[user_id]
#     except KeyError:
#         print(f"Пользователь не найден:" {user_id})
#         raise

#     users = {1: "Alice"}
#     try:
#         print(load_user(users, 2))
#     except KeyError:
#         print("Ошибка")



# class ConfigError(Exception):
#     pass

#     def load_port(raw_port):
#         try:
#             return int(raw_port)
#         except ValueError as e:
#             raise ConfigError("Поле PORT должно быть целым числом") from e

#     try:
#         load_port("abc")
# except ConfigError as e:
#     print()



# class EmployeeError(Exception):
#     pass

# class EmployeeNotFoundError(EmployeeError):
#     pass

# class SalaryValidationError(EmployeeError):
#     pass

#     def find_emploee(employees, emp_id):
#         if emp_id not in employees:
#             raise EmployeeNotFoundError(F"Сотрудник {emp_id} не найден")
#         return employees[emp_id]

# def validate_salary(value):
#     if value < 0:
#         raise SalaryValidationError("ЗП не может быть отрицательным")

# try:
#     find_emploee({}, 10)
# except EmployeeNotFoundError as e:
#     print(e.message2)
# except SalaryValidationError as e:
#     print(e)




def normalize_percent(x):
    assert isinstance(x, int), "Должен быть числом"
    if not 0 <= x <= 100:
        raise ValueError("Процент должен быть от 0 до 100.")
    return x / 100

print(normalize_percent(25))
print(normalize_percent("abc"))