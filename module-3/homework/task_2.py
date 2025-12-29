# задание 1


# def calculate(expr):
   
#     expr = expr.replace(' ', '')

#     operators = ['+', '-', '*', '/']

#     for op in operators:
#         if op in expr:
#             parts = expr.split(op)
#             if len(parts) == 2:
#                 try:
#                     left = float(parts[0])
#                     right = float(parts[1])
#                     if op == '+':
#                         return left + right
#                     elif op == '-':
#                         return left - right
#                     elif op == '*':
#                         return left * right
#                     elif op == '/':
#                         if right == 0:
#                             return "Ошибка: деление на ноль!"
#                         else:
#                             return left / right
#                 except ValueError:
#                     return "Ошибка: введены некорректные числа!"
#     return "Ошибка: выражение должно содержать один из операторов +, -, *, /"

# expression = input("Введите арифметическое выражение вида число оператор число (например 23+12): ")

# result = calculate(expression)

# print("Результат:", result)



# задание 2



numbers = [-6, -8, -5, -6, 3, -7, 4, 4, -5, 3, 3, -5, -9, 6, -2, -6, -3, 3, -4, 9, 0]

print(numbers)

min_value = min(numbers)
max_value = max(numbers)

count_negative = sum(1 for x in numbers if x < 0)
count_positive = sum(1 for x in numbers if x > 0)
count_zero = sum(1 for x in numbers if x == 0)

print(f"Минимальное значение: {min_value}")
print(f"Максимальное значение: {max_value}")
print(f"Количество отрицательных элементов: {count_negative}")
print(f"Количество положительных элементов: {count_positive}")
print(f"Количество нулей: {count_zero}")