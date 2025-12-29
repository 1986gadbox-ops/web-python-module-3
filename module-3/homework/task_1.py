
list1 = [4,2,9,7,5,9,0,3,1,6]
list2 = [10,7,4,1,8,3,6,0,5,2]

print(list1)
print(list2)

# 1
list_all = list1 + list2
print("оба списка", list_all)

# 2
list_all1 = list(set(list_all))
print("без повторений", list_all1)

# 3
list_all2 = list(set(list1).intersection(set(list2)))
print("Общие элементы:", list_all2)

# 4
set1 = set(list1)
set2 = set(list2)
list_all3 = list((set1 - set2).union(set2 - set1))
print("Уникальные элементы каждого списка:", list_all3)

# 5
list_all4 = [min(list1), max(list1), min(list2), max(list2)]
print("Минимальное и максимальное значения каждого списка:", list_all4 )