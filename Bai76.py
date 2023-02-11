def timMin(arr):
    min = arr[0]
    for i in arr:
        if min > i:
            min = i
    return min
arr = list(map(float, input().split()))
print(timMin(arr))
