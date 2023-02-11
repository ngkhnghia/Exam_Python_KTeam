def hoanDoiDanhSach(list1, list2):
    a = len(list1) // 2
    b = len(list2) // 2
    result1 = list1[:a] + list2[b:]
    result2 = list2[:b] + list1[a:]
    return result1, result2

list1 = list(input().split())
list2 = list(input().split())
result1, result2 = hoanDoiDanhSach(list1, list2)
print(*result1)
print(*result2)