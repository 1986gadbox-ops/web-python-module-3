# file = open("file.txt", "r")
# print(file.read(1))
# print(file.read(1))
# file.close()

# r - Чтение
# w - запись с отчисткой
# a - дозапись текста в конец файла
# x - создает новый файл
# t - текстовый режим
# b - бинарный режим
# + - чтение и запись файла
# -----------------------------------
# file = open("C:\Windows") - ошибка

# file = open("C:/Windows") - Лучший способ



# file = open("file.txt", "w")
# file.write("54321")
# file.close()



# file = open("file.txt", "a", encoding="utf-8")
# file.write("- добавили в конец")
# file.close()



# f = open("file.txt", "a", encoding="utf-8")
# f.write("1,2,3\n")
# f.write("4,5,6\n")
# f.write("7,8,9")
# f.close()


# f = open("file.txt", "r", encoding="utf-8")
# print(f.readline().strip())
# print(f.readline().strip())
# print(f.readline().strip())


# for line in f:
#     print(line.strip())


# with open("file.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())






# задание 1

# with open("inventory.txt", "x", encoding="utf-8") as f:
#     for line in f:
#         print(line.atrip())


# file = open("inventory.txt", "w", encoding="utf-8")
# file.write("2024-01-01,яблоко,IN,50\n"
#            "2024-01-02,банан,IN,30\n"
#            "2024-01-03,яблоко,OUT,10\n"
#            "2024-01-03,груша,OUT,5\n"
#            "2024-01-04,груша,IN,20\n"
#            "2024-01-05,банан,OUT,40\n"
#            "2024-01-06,яблоко,OUT,5")
# file.close()




# with open("inventory.txt", "r", encoding="utf-8") as f:
#      for line in f:
#          print(line.strip())

 inventory = [
    ("2024-01-01", "яблоко", "IN", "50")
    ("2024-01-02", "банан", "IN,30")
    ("2024-01-03,яблоко,OUT,10")
    ("2024-01-03,груша,OUT,5")
    ("2024-01-04,груша,IN,20")
    ("2024-01-05,банан,OUT,40")
    ("2024-01-06,яблоко,OUT,5")
 ] 

date = {}
product = {}
operation_type = {}
quantity = {}

for inventory in inventorys:
    if inventory [0] not in quantity:
        quantity [inventory[0]] = set()
    quantity[inventory[0]].add(inventory[1])
 print(quantity)