def trungBinhCong(arr):
    tong = sum(arr)
    result = tong / len(arr)
    return result
arr = list(map(float, input().split()))
print(trungBinhCong(arr))