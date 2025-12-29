# word = input("Введите слово: ")

# counts = {}

# for char in word:
#     counts[char] = counts.get(char, 0) + 1

# for char, count in counts.items():
#     print(f"{char}={count}")


# my_dict = {}

# n = int(input("Сколько пар ключ-значение хотите добавить? "))

# for i in range(n):
#     key = input(f"Введите название {i+1}: ")
#     value = input(f"Введите значение {key}: ")
#     my_dict[key] = value

# print(my_dict)


# prices ={"bread": 20, "milk": 80, "cheese": 25}
# cart = {"bread": 2, "cola":1, "milk": 3}

# total = 0
# for key, value in cart.items():
#     if key in prices:
#         total += prices.get(key) * value
#     else:
#         print("цена на данный товар отсутствует")

# print(total)


text="Hello World"
replacements = {"e": 1, "l": 0, "o": 2, "r": 3}

result = ""

for char in text:
    result += str(replacements.get(char,char))

    print(result)