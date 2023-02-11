try:
    n = int(input())
    if n < 0:
        print('n > 0')
    else:
        if n == 0 or n == 1:
            print('{} khong la so nguyen to'.format(n))
        else:
            for i in range(2, n + 1, 1):
                if n % i == 0:
                    break
            if i >= n:
                print('{} la so nguyen to'.format(n))
            else:
                print('{} khong la so nguyen to'.format(n))
except:
    print('dinh dang dau vao khong hop le')