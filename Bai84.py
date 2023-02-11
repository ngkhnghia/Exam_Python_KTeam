def timPhanTuLonNhat(arr):
    max_ = max(arr)
    count = arr.count(max_)
    index = []
    for i in range(len(arr)):
        if arr[i] == max_:
            index.append(i)
    return max_, count, index
arr = list(map(int, input().split()))
max, count, index = timPhanTuLonNhat(arr)
print(max)
print(count)
print(*index)