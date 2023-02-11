def danhSachSoNguyenTo(arr):
    result = list([])
    for value in arr:
        if value == 2:
            result.append(value)
        elif value == 0 or value == 1:
            continue
        else:
            chiSo = 0
            for chiSo in range(2, len(arr), 1):
                if value % chiSo == 0:
                    break
            if chiSo == len(arr) - 1:
                result.append(value)
    return result
arr = list(map(int, input().split()))
print(*danhSachSoNguyenTo(arr))