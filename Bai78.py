def kiemTraDanhSachGiam(arr):
        max = arr[0]
        for i in range(len(arr)):
            if max < arr[i]:
                return False
            max = arr[i]
        return True
arr = list(map(float, input().split()))
if kiemTraDanhSachGiam(arr):
    print('True')
else:
    print("False")