# num_str1 = input("Ведите цифру от 0 до 9: ")
# num_str2 = input("Ведите вторую цифру от 0 до 9: ")
# num_str3 = input("Ведите третью цифру от 0 до 9: ")

# num1 = int(num_str1)
# num2 = int(num_str2)
# num3 = int(num_str3)

# print (num1, num2, num3, sep ='')


# задание 2

# n = input("Введите число из четырех цифр: ")

# product = 1
# for digit in n: 
#     if digit.isdigit():
#         product *= int(digit)
# print(f"{product}")



# задание 3


n = input("Введите количество метров: ")
num = int(n)
san = (num * 100)
dec = (num * 10)
mill = (num * 1000)
mil = (num * 0.000621)
print(f"сантиметров: {san}, дециметров: {dec}, миллиметров: {mill}, миль: {mil}")



