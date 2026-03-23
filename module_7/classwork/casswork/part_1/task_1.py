# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n - 1):
#         swapped = False
#         for j in range(n - 1 - i):
#            if arr[j] > arr[j+1]:
#             # 2 1 = 1 2
#                 arr[j], arr[j + 1] = arr[j+1], arr[j]
#                 swapped = True

#         if not swapped:
#             break

#     return arr

# print(bubble_sort([1,4,6,2,8]))
