try:
    n = int(input())
    if 1 <= n <= 9:
        for i in range(1, 10, 1):
            print('{} x {} = {}'.format(n, i, n*i))
    else:
        print('chi tinh duoc bang cuu chuong tu 1 den 9 thoi')
except:
    print('dinh dang dau vao khong hop le!')