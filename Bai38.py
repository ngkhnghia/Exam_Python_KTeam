try:
    n = int(input())
    if n <= 0:
        print('n > 0')
    else:
        sum = 0
        for i in range(1, n, 1):
            if n % i == 0:
                sum += i
        if sum == n:
            print('{} la so hoan hao'.format(n))
        else:
            print('{} khong la so hoan hao'.format(n))
except:
    print('dinh dang dau vao khong hop le')