def phanTuLe(arr):
    arr = [x for x in arr if x % 2 == 1]
    return arr
arr = list(map(int, input().split()))
print(*phanTuLe(arr))