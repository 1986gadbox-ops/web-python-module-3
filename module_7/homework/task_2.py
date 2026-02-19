
def calculate(expr):
   
    expr = expr.replace(' ', '')

    operators = ['+', '-', '*', '/']

    for op in operators:
        if op in expr:
            parts = expr.split(op)
            if len(parts) == 2:
                try:
                    left = float(parts[0])
                    right = float(parts[1])
                    if op == '+':
                        return left + right
                    elif op == '-':
                        return left - right
                    elif op == '*':
                        return left * right
                    elif op == '/':
                        if right == 0:
                            return "Ошибка: деление на ноль!"
                        else:
                            return left / right
                except ValueError:
                    return "Ошибка: введены некорректные числа!"
    return "Ошибка: выражение должно содержать один из операторов +, -, *, /"

expression = input("Введите арифметическое выражение вида число оператор число (например 23+12): ")

result = calculate(expression)

print("Результат:", result)







