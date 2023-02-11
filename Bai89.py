def dsPhanTuRieng(list1, list2):
    result = [i for i in list1 if i not in list2] + [i for i in list2 if i not in list1]
    return result

list1 = input().split()
list2 = input().split()
print(*dsPhanTuRieng(list1, list2))