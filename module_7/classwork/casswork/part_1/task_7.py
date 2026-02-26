





# def shell_sort(arr):
#     n = len(arr)
#     gap = n // 2

#     while gap > 0:
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i

#             while j >= gap and arr[j - gap] > temp:
#                 arr[j] = arr[j - gap]
#                 j -= gap
#             arr[j] = temp
#         gap //= 2
#     return arr

# ----------

# [8,3,7,1]
# n = 4
# gap = 2

# i = 2
# temp = 7
# j = 2

# arr[j - gap] = arr[0] = 8
# j = 0
# -----------
# i = 3
# temp = 1
# j = 3
# arr[j - gap] = arr[3 - 2] = arr[1] = 3
# [7, 1, 8, 3]
# ---------------
# gap = 1
# [1, 7, 3, 8]
# [1 ,3 ,7 ,8]



# алгоритм быстрой сортировки

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[0]
#     less = [i for i in[1:] if i <= pivot]
#     greater = [i for i in arr[1:] if i > pivot]

#     return quick_sort(less) + [pivot] + quick_sort(greater)

    # ---------

# [1, 5, -2, 3]
# pivot = 1
# [5, -2, 3]
# less = [-2]
# greater = [5, 3]
# quick_sort([-2]) + [1] + quick_sort([5,3])

# ----------

# [5, 3]
# pivot = 5
# less = [3]
# greater = []
# quick_sort([3]) 




# задача 6



# clients = [
#     (1, "111", "a@x.com"),
#     (2, "111", "b@x.com"),
#     (3, "222", "c@x.com"),
#     (4, "333", "c@x.com"),
#     (5, "444", "d@x.com"),
# ]

# phones = {}
# emails = {}

# for id, name, email in clients:
#     phones.setdefault(name, set()).add(id)
#     emails.setdefault(email, set()).add(id)
# dubliceites = []    
# for o in(phones, emails):
#     for ids in o.values():
#         if len(ids) > 1:
#             dubliceites.append(ids)
# dubliceites_ids = set()
# for n in dubliceites:
#     dubliceites_ids = n
#     unique_clients = [cid for cid, _, _ in clients if cid not in dubliceites_ids]

#     print("Группы дублей (по id клиентов):")
# for i, group in enumerate(dubliceites, 1):
#     print(f"Группа {i}: {sorted(group)}")

# print("Клиенты без дублей (id):", unique_clients)
# print("Количество чистых клиентов:", len(unique_clients))





# задача 7



logs = [
    ("ivan", "d1", "login"),
    ("ivan", "d1", "view"),
    ("ivan", "d2", "login"),
    ("olga", "d1", "login"),
    ("petr", "d2", "error"),
    ("anna", "d1", "login"),
    ("anna", "d2", "view"),
]

user_actions = {}
user_actions_count = {}
for user, day, actions in logs:
    user_actions_count[user] = user_actions_count.get(user, 0) + 1
    if user not in user_actions:
        user_actions[user] = set()
        user_actions[user].add(actions)

    if user not in user_actions_count:
        user_actions_count[user] = 0

error_no_login = set()
for user, actions in user_actions.items():
    if "error" in actions and "login" not in actions:
        error_no_login.add(user)

active_day = set()
user_days = {}
for user, day in user_days.items:
    if user_days(day) > 1:
        active_day.add(user)


print(active_day)







