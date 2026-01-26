# def func_1():
#     result = []
#     for i in range(5):
#         result.append(i)
#     return result

# print(func_1())


# def func_2():
#     for i in range(5):
#         yield i

# gen = func_2()
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))


# for i in func_2():
#     print(i)



# def factorial(n):
    # базовый случай
    # if n <= 1:
    #     return 1

        # рекрусивный шаг
        # 9! = 9 * 8 * 7 * 6 * 5 ...

#     return n * factorial(n - 1)

# print (factorial(5))



# задача 1

# def power(x, n):
#     if n == 1:
#         return x
#     # рекрусивный шаг
#     return x * power(x, n - 1)

# print(power(2,3))



# задача 2


# def power(a, b):
#     if a > b:
#         return 0
#     else:
#         return a + power(a + 1, b)

# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))

# result = power(a, b)
# print(f"cумма чисел от {a} до {b} равна {result}")




# задача 3



# def stars(n):
#     if n <= 0:
#         return  
#     else:
#         print('*', end ='')  
#         stars(n - 1)  


# N = int(input("Введите число количество звёздочек: "))

# stars(N)
# print()  



# задача 4 крестики нолики


# import random

# board = [" " for _ in range(9)]
# wins = [
#     (0,1,2), (3,4,5), (6,7,8),
#     (0,3,6), (1,4,7), (2,5,8),
#     (0,4,8), (2,4,6)
# ]

# def print_board():
#     print(f"{board[0]} | {board[1]} | {board[2]}")
#     print(f"--+---+--")
#     print(f"{board[3]} | {board[4]} | {board[5]}")
#     print(f"--+---+--")
#     print(f"{board[6]} | {board[7]} | {board[8]}")

# def check_wins(s):
#     for a,b,c in wins:
#         if board[a] == board[b] == board[c] == s:
#             return True
#     return False

# def is_draw():
#     return " " not in board

# def computer_move():
#     empty_cells = [i for i in range(9) if board[i] == " "]
#     if not empty_cells:
#         return

#     move = random.choice(empty_cells)
#     board[move] = "0"

# def tic_tac_toe():
#     while True:
#         print_board()
#         move = int(input("Ход(0-9):"))

#         if move < 0 or move > 8 or board[move] != " ":
#             print("Неверный ход")
#             continue

#         board[move] = "x"

#         if check_wins("x"):
#             print_board()
#             print("Победа")
#             break

#         if is_draw():
#             print_board()
#             print("Ничья")
#             break


#         computer_move()

#         if check_wins("0"):
#             print_board()
#             print("Поражение")
#             break

#         if is_draw():
#             print_board()
#             print("Ничья")
#             break

# tic_tac_toe()


# задача 5


import random

nums = [random.randint(-50,50) for _ in range(100)]

def min_innterval_pos(i, best_pos = 0, best_sum = None):
    if i + 10 > len(nums):
        return best_pos

    summ = sum(nums[i: i + 10])
    if best_sum == None or summ < best_sum:
        best_sum = summ
        best_position = i

    return min_innterval_pos(i + 1,best_pos, best_sum)

best_pos = min_innterval_pos(0)
print(f"{nums[best_pos:best_pos + 10]}")



