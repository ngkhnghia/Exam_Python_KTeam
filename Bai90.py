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
    for i in range(m):
        print(*danhSach[n*i:n*i+n])

try:
    m , n = int(input()), int(input())
    
    if m <= 0 or n <= 0:
        print("m, n phai lon hon 0")
    else:
        danhSach = nhapDanhSach(m, n)
        if danhSach == None:
            print("Danh sach khong dung kich thuoc")
        else:
            xuatDanhSach(m, n, danhSach)
            pass
        

except:
    print("m, n phai la so nguyen")