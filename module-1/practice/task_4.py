# задание 1


# def gcd(a, b):
#     if b == 0:
#         return abs(a)
#     else:
#         return gcd(b, a % b)

# a = int(input("Введите первое целое число: "))
# b = int(input("Введите второе целое число: "))

# result = gcd(a, b)
# print(f"Наибольший общий делитель чисел {a} и {b} равен {result}.")


# задание 2

# import random

# def generate_number():
#     digits = list('0123456789')
#     random.shuffle(digits)
#     if digits[0] == '0':
#         for i in range(1, 10):
#             if digits[i] != '0':
#                 digits[0], digits[i] = digits[i], digits[0]
#                 break
#     return ''.join(digits[:4])

# def count_bulls_and_cows(secret, guess):
#     bulls = sum(s == g for s, g in zip(secret, guess))
#     cows = 0
#     for digit in set(guess):
#         cows += min(secret.count(digit), guess.count(digit))
#     cows -= bulls
#     return bulls, cows

# def game(secret, attempts=0):
#     guess = input("Введите 4-значное число с разными цифрами: ")
#     if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
#         print("Некорректный ввод! Попробуйте ещё раз.")
#         return game(secret, attempts)
    
#     attempts += 1
#     bulls, cows = count_bulls_and_cows(secret, guess)

#     if bulls == 4:
#         print(f"Поздравляю! Вы угадали число {secret} за {attempts} попыток.")
#         return
#     else:
#         print(f"Быки: {bulls}, Коровы: {cows}")
#         return game(secret, attempts)

# if __name__ == "__main__":
#     secret_number = generate_number()
#     print("Игра 'Быки и коровы'. Угадайте 4-значное число!")
#     game(secret_number)




# задание 3

# def is_valid(x, y, board_size, board):
#     return 0 <= x < board_size and 0 <= y < board_size and not board[y][x]

# def print_board(board):
#     for row in board:
#         print(' '.join(f"{cell:2}" for cell in row))
#     print()

# def solve_knight(x, y, move_number, board, moves, board_size):

#     if move_number == board_size * board_size:
#         return True

  
#     for dx, dy in moves:
#         next_x, next_y = x + dx, y + dy
#         if is_valid(next_x, next_y, board_size, board):
#             board[next_y][next_x] = move_number + 1
#             if solve_knight(next_x, next_y, move_number + 1, board, moves, board_size):
#                 return True
        
#             board[next_y][next_x] = 0
#     return False

# def main():
#     board_size = 6 
#     board = [[0]*board_size for _ in range(board_size)]

#     start_x = int(input("Введите x начальной клетки (0-5): "))
#     start_y = int(input("Введите y начальной клетки (0-5): "))

#     board[start_y][start_x] = 1

#     moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
#              (2, 1), (1, 2), (-1, 2), (-2, 1)]

#     if solve_knight(start_x, start_y, 1, board, moves, board_size):
#         print("Путь найден! Вот решение:")
#         print_board(board)
#     else:
#         print("Путь не найден.")

# if __name__ == "__main__":
#     main()


# задание 4



# import random

# def create_board():
#     board = list(range(1, 16)) + [0]
#     while True:
#         random.shuffle(board)
#         if is_solvable(board):
#             return [board[i*4:(i+1)*4] for i in range(4)]

# def is_solvable(board):
#     arr = [x for x in board if x != 0]
#     inversions = 0
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 inversions += 1
    
#     empty_row = 4 - (board.index(0) // 4)
    
#     if empty_row % 2 == 0:
#         return inversions % 2 == 1
#     else:
#         return inversions % 2 == 0

# def print_board(board):
#     print()
#     for row in board:
#         print(' '.join(f"{num:2}" if num != 0 else "  " for num in row))
#     print()

# def find_empty(board):
#     for y in range(4):
#         for x in range(4):
#             if board[y][x] == 0:
#                 return x, y

# def move_tile(board, direction):
#     x, y = find_empty(board)
#     dx, dy = 0, 0
#     if direction == 'w': dy = 1      
#     elif direction == 's': dy = -1   
#     elif direction == 'a': dx = 1    
#     elif direction == 'd': dx = -1   
#     else:
#         print("Используйте w(up), s(down), a(left), d(right)")
#         return False

#     new_x, new_y = x + dx, y + dy
#     if 0 <= new_x < 4 and 0 <= new_y < 4:
#         board[y][x], board[new_y][new_x] = board[new_y][new_x], board[y][x]
#         return True
#     else:
#         print("Невозможный ход.")
#         return False

# def is_solved(board):
#     solved = list(range(1, 16)) + [0]
#     flat = [num for row in board for num in row]
#     return flat == solved

# def play():
#     board = create_board()
#     print("Игра Пятнашки. Используйте w(up), s(down), a(left), d(right) для ходов. Введите q для выхода.")
#     print_board(board)
    
#     while True:
#         move = input("Ваш ход (w/a/s/d): ").strip().lower()
#         if move == 'q':
#             print("Выход из игры.")
#             break
#         if move_tile(board, move):
#             print_board(board)
#             if is_solved(board):
#                 print("Поздравляем! Вы собрали пазл!")
#                 break

# if __name__ == "__main__":
#     play()
