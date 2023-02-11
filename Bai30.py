try:
    n = int(input())
    if 1 <= n <= 10:
        for i in range(n , 0, -1):
            for k in range(i , 0, -1):
                print(k, end= ' ')
            print('')
    else:
        print('vui long nhap gia tri tu 1 den 9')
except:
    print('dinh dang dau vao khong hop le')