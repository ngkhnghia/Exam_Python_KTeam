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
    result = []
    for i in range(len(matrix)):
        if matrix[i] in result:
            continue
        flag = True
        for j in range(m):
            if flag == False:
                break
            if (i-i%n)/n == j:
                continue
            for k in range(n):
                if matrix[i] == matrix[j*n+k]:
                    break
            if k == n-1 and matrix[i] != matrix[j*n+k]:
                flag = False
        if flag == True:
            result.append(matrix[i])
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