lst = [5, -2, 7, 0, -3, 8, 1]

def special_sort(lst):
    avg = sum(lst) / len(lst)
    length = len(lst)

    if avg > 0:
        first_part = sorted(lst[:3])
    else:
        first_part = sorted(lst[:3], reverse=True)

    rest = lst[3:]
    rest.reverse() 

    sorted_list = first_part + rest
    return sorted_list

print("Изначальный список:", lst)
result = special_sort(lst)
print("Результат:", result)

------------------------------------

grades = []
for i in range(10):
    while True:
        grade = int(input(f"Введите оценку {i+1} (от 1 до 12): "))
        if 1 <= grade <= 12:
            grades.append(grade)
            break
        else:
            print("Некорректная оценка. Попробуйте снова.")

def display_grades(grades_list):
    print("Оценки:", grades_list)

def reattempt(grades_list):
    index = int(input("Введите номер элемента для пересдачи (1-10): ")) - 1
    if 0 <= index < len(grades_list):
        while True:
            new_grade = int(input("Введите новую оценку (от 1 до 12): "))
            if 1 <= new_grade <= 12:
                grades_list[index] = new_grade
                print(f"Элемент №{index+1} обновлен.")
                break
            else:
                print("Некорректная оценка. Попробуйте снова.")
    else:
        print("Некорректный номер элемента.")

def check_scholarship(grades_list):
    avg = sum(grades_list) / len(grades_list)
    if avg >= 10.7:
        print("Вы выходите на стипендию!")
    else:
        print("К сожалению, стипендия не полагается.")

def sort_grades(grades_list, ascending=True):
    sorted_list = sorted(grades_list, reverse=not ascending)
    print("Отсортированный список оценок:")
    display_grades(sorted_list)

while True:
    print("\n Меню:")
    print("1. Вывести оценки")
    print("2. Пересдача экзамена")
    print("3. Выходит ли стипендия")
    print("4. Вывести отсортированный список по возрастанию")
    print("5. Вывести отсортированный список по убыванию")
    print("6. Выход")
    choice = input("Выберите действие: ")

    if choice == '1':
        display_grades(grades)
    elif choice == '2':
        reattempt(grades)
    elif choice == '3':
        check_scholarship(grades)
    elif choice == '4':
        sort_grades(grades, ascending=True)
    elif choice == '5':
        sort_grades(grades, ascending=False)
    elif choice == '6':
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")

--------------------------------------

def bubble_sort_improved(lst):
    n = len(lst)
    for i in range(n):
        count_swaps = 0
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                count_swaps += 1
        if count_swaps == 0:
            break
    return lst

list_to_sort = [64, 34, 25, 12, 22, 11, 90]
print("До сортировки:", list_to_sort)
sorted_list = bubble_sort_improved(list_to_sort)
print("После сортировки:", sorted_list)