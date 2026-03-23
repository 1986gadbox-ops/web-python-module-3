# text = "python"
# print(text[0:7])
# print(text[0:3])
# print(text[::-1])

# превращает в заглавные буквы
# print(text.upper())
# в маленькие
# print(text.lower())
# заглавные буквы
# print(text.capitalize())


# поиск по порядку
# print(text.find("y"))
# print(text.index("o"))


# замена
# text = "hello world, hello, hello"
# print(text.replace("hello", "hi",))


# text = "python 123"
# только буквы
# print(text.isalpha())

# только цифры
# print(text.isdigit())

# только буквы и цифры
# print(text.isalnum())

# пробелы
# print(text.isspace())

# заглавные
# print(text.isupper())

# прописные
# print(text.islower())

# отчищает
# text = "*** Python***"
# print(text.strip("*"))

# с лева
# print(text.lstrip()) 

# с права
# print(text.rstrip())


# text = "яблоко, апельсин, банан"


# разбить по пробелам


# выводит в строку
# u =", ".join(f)
# print(f, u)


# text = "row_1\nrow_2\nrow_3"
# sl = text.splitlines()
# print(sl)

# f = text.split(", ")
# u = ", ".join(f)



# tuple_1 = (1,2,3)

# tuple_3 = 1,2,3

# print(tuple_1)
# print(tuple_2)
# print(tuple_3)

# tuple_2 = tuple(range(0,11))

# print(tuple_2[0])
# print(tuple_2[2:5])


# num1, num2, num3, num4 = (1,2,3,4)
# print(num1, num2, num3, num4)

# num1,*other, last_el = tuple(range(0,11))
# print(num1, other, last_el)


# Сложение
# tuple1 = (1,2)
# tuple2 = (3,4)
# result = tuple1 + tuple2
# print(result)


# повторение
# pattern =("a", "b")
# repeated = pattern * 2
# print(repeated)


# принадлежность
# f = ("apple", "banana")
# print ("apple" in f)


# numbers = (1,2,3,2,4,5,2)

# количество
# print(numbers.count(2))

# индекс первого вхождения
# print(numbers.index(2))


# num_tuple = tuple(range(0,5))
# for index, num in enumerate (num_tuple):
#     print(index, num)


# кортежи в цикле(интерирование)
# tuple_1_sym = ("b")
# tuple_2_sym = ("b",)
# print(tuple_1_sym, tuple_2_sym)


# задача 1

# text = input("введиде слово: ")
# print(text[::-1])

# задача 2
# text = input("Введите строку: ")
# print(text[:])



# задача 3
# text = input("Введите строку: ")
# text2 = input("Введите символ для поиска: ")

# print(text.count(text2))


# задача 4

# text = input("Введите строку: ")
# text2 = input("Введите слово для поиска: ")

# print(text.count(text2))


# задача 5

# text = input("Введите текст: ")
# text2 = input("Введите слово для поиска: ")
# text3 = input("Введите слово для замены: ")

# print(text.replace(text2,text3))



# задача 6

# text = "как дела. все хорошо на 5 с плюсом"



# задача 7


# text = input("Введите элементы списка целых чисел через пробел: ")
# numbers = list(map(int, text.strip().split()))
# num = int(input("Введите число для подсчёта в списке: "))
# count = numbers.count(num)
# print(f"Число {num} встречается в списке {count} раз(а).")


# задача 8


# text = input("Введите элементы списка целых чисел через пробел: ")
# numbers = list(map(int, text.strip().split()))
# total_sum = sum(numbers)
# average = total_sum / len(numbers) if numbers else 0
# print(f"Сумма элементов: {total_sum}")
# print(f"Среднее арифметическое: {average}")



# задача 9


# numbers = [-6, -8, -5, -6, 3, -7, 4, 4, -5, 3, 3, -5, -9, 6, -2, -6, -3, 3, -4, 9, 0]
# count_negative = sum(1 for x in numbers if x < 0)
# num_even = 
# print(f"количество отрицательных элементов {count_negative}")






# функции





