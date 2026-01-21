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