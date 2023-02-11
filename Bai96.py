try:
    n = int(input())
    if n < 0:
        print("Vui long nhap so nguyen duong!")
    else:
        tup = (n, *(n for i in range(n)))
        print(tup)
except:
    print("Dinh dang dau vao khong hop le!")