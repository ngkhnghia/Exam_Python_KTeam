def nhapDanhSach(m, n):
    result = []
    for i in range(m):
        row = input().split()
        if len(row) != n:
            return None
        else:
            for i in range(n):
                result.append(row[i])
    return result

def xuatDanhSach(m, n, danhSach):
    result =[]
    for i in range(m):
        arr = danhSach[i*n:(i+1)*n]
        max = 0
        index = -1
        for j in range(len(arr)):
            if len(arr[j]) > max:
                max = len(arr[j])
                index = j
        result.append(arr[index])
    return result

try:
    m, n = int(input()), int(input())
    if m <=0 or n <= 0:
        print("Vui long nhap kich thuoc danh sach la so nguyen duong")
    else:
        danhSach = nhapDanhSach(m, n)
        if danhSach == None:
            print("Danh sach hai chieu khong dung kich thuoc!")
        else:
            print(*xuatDanhSach(m, n, danhSach))
except:
    print("Dinh dang dau vao khong hop le!")