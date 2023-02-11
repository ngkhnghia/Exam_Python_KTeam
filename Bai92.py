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

def xuatDanhSach(m, n, matrix):
    result = [x for x in matrix]
    for i in range(m):
        for j in range(n):
            result[j*m+i] = matrix[i*n+j]
    return result

try:
    m, n = int(input()), int(input())
    if m <=0 or n <= 0:
        print("Vui long nhap kich thuoc danh sach la so nguyen duong")
    else:
        matrix = nhapDanhSach(m, n)
        if matrix == None:
            print("Danh sach hai chieu khong dung kich thuoc!")
        else:
            print(*xuatDanhSach(m, n, matrix))
except:
    print("Dinh dang dau vao khong hop le!")