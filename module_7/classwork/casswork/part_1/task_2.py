# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
# # [10,0,-2,4,8]
# # [-2,0,4,8,10]
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1

#         arr[j + 1] = key

#     return arr
# print(insertion_sort([10,0,-2,4,8]))



# задача 1

# network = {"Me": {"Alice", "Bob"},
#             "Alice": {"Me", "Charlie", "Bob"},
#             "Bob": {"Me", "David", "Eva"},
#             "Charlie": {"Alice"},
#             "David": {"Alice", "Bob"},
#             "Eva": {"Bob"},
#             }


# def friends_of_friends(network, user):
#     user_friends = network.get(user, set())

#     friends_of_friends = set()
#     for friend in user_friends:
#         friends_of_friend = network.get(friend, set())
#         friends_of_friends.update(friends_of_friend)

#     friends_of_friends.discard(user)
#     friends_of_friends.difference_update(user_friends)
#     return friends_of_friends

# result = friends_of_friends(network, "Bob")
# print(result)




# задача 2


# import random

# tasks = []

# for i in range(10):
#     tasks.append({
#         "id": f"t_{i}",
#         "assignee": random.choice(["ivan", "olga", "petr", "anna", "oleg"]),
#         "status": random.choice(["in progress", "blocked", "in review", "waiting vendor"]),
#         "days in status": random.randint(0, 10)
#     })

# progress = set()

# for task in tasks:
#     if task ["status"] == "in progress" and task ["days in status"] > 7:
#         progress.add(task["assignee"])
#     print(progress)


# status_assignee = {}
# for task in tasks:
#     status = task["status"]
#     assignee = task["assignee"]
#     if status not in status_assignee:
#         status_assignee [status] = set()
#     status_assignee[status].add(assignee)
# result = {}
# for status in status_assignee:
#     if len (status_assignee[status]) == 1:
#         result[status] = list(status_assignee[status]) [0]
# print(result)

# max days = 0
# assignee = 0
# for task in tasks:
#     if task["status"] == "in progress" or task["status"] == "blocked":
#         max days = task["day_in_status"]
#         assignee = task["assignee"]
# print()




# алгоритм сортировки выбором

# def selection_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         min_idx = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# print(selection_sort([7,9,4,2,1]))



# # сортировка слияния

# def merge_sort(arr):
#     if len(arr) == 1:
#         return arr

#     mid = len(arr) // 2

#     left_part = merge_sort(arr[:mid])
#     right_part = merge_sort(arr[mid:])

#     return merge(left_part, right_part)

# def merge(left_part, right_part):
#     i = 0
#     j = 0
#     result = []
#     while i < len(left_part) and j <len(right_part):
#         if left_part[i] <= right_part[j]:
#             result.append(left_part[i])
#             i+=1
#         else:
#             result.append(right_part[j])
#             j+=1

#     result.extend(left_part[i:])
#     result.extend(right_part[j:])

#     return result

#     print(merge_sort([7,9,4,2,1]))




