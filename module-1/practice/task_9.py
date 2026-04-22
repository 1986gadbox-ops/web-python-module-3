# задание 1

# def custom_sort(lst):
#     n = len(lst)
#     third = n // 3

#     avg = sum(lst) / n if n > 0 else 0

#     first_third = lst[:third]
#     second_third = lst[third:2*third]
#     rest = lst[2*third:]

#     if avg > 0:
#         sorted_part = sorted(first_third) + sorted(second_third)
#     else:
#         sorted_part = sorted(first_third) + second_third

#     rest_reversed = rest[::-1]

#     result = sorted_part + rest_reversed
#     return result

# lst = [3, 1, 2, 7, 6, 8, -1, 0, 5]
# print(custom_sort(lst))





# задание 2


# def print_grades(grades):
#     print("Оценки студента:", grades)

# def resit_exam(grades):
#     try:
#         index = int(input("Введите номер оценки для пересдачи (1-10): ")) - 1
#         if not 0 <= index < len(grades):
#             print("Неверный номер оценки.")
#             return
#         new_grade = int(input("Введите новую оценку (1-12): "))
#         if not 1 <= new_grade <= 12:
#             print("Оценка должна быть от 1 до 12.")
#             return
#         grades[index] = new_grade
#         print(f"Оценка под номером {index+1} успешно изменена на {new_grade}.")
#     except ValueError:
#         print("Ввод должен быть числом.")

# def check_scholarship(grades):
#     avg = sum(grades) / len(grades)
#     if avg >= 10.7:
#         print(f"Средний балл: {avg:.2f}. Стипендия положена!")
#     else:
#         print(f"Средний балл: {avg:.2f}. Стипендия не положена.")

# def sort_grades(grades):
#     order = input("Сортировка (введите 'asc' для возрастания или 'desc' для убывания): ").strip().lower()
#     if order == "asc":
#         sorted_grades = sorted(grades)
#     elif order == "desc":
#         sorted_grades = sorted(grades, reverse=True)
#     else:
#         print("Некорректный ввод.")
#         return
#     print("Отсортированные оценки:", sorted_grades)

# def main():
#     print("Введите 10 оценок студента (от 1 до 12):")
#     grades = []
#     while len(grades) < 10:
#         try:
#             grade = int(input(f"Оценка {len(grades)+1}: "))
#             if 1 <= grade <= 12:
#                 grades.append(grade)
#             else:
#                 print("Оценка должна быть в диапазоне от 1 до 12.")
#         except ValueError:
#             print("Пожалуйста, введите число.")

#     while True:
#         print("Меню:")
#         print("1 - Вывод оценок")
#         print("2 - Пересдача экзамена")
#         print("3 - Проверка стипендии")
#         print("4 - Сортировка оценок")
#         print("0 - Выход")

#         choice = input("Выберите пункт меню: ").strip()

#         if choice == "1":
#             print_grades(grades)
#         elif choice == "2":
#             resit_exam(grades)
#         elif choice == "3":
#             check_scholarship(grades)
#         elif choice == "4":
#             sort_grades(grades)
#         elif choice == "0":
#             print("Выход из программы.")
#             break
#         else:
#             print("Некорректный выбор. Попробуйте снова.")

# if __name__ == "__main__":
#     main()




# задание 3


def improved_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

lst = [64, 34, 25, 12, 22, 11, 90]
print("Исходный список:", lst)
improved_bubble_sort(lst)
print("Отсортированный список:", lst)