try:
    n = int(input())
    if n < 0:
        print('n >= 0')
    else:
        for i in range(1, n + 1, 1):
            if n % i == 0:
                print(i, end= ' ')
except:
    print('dinh dang dau vao khong hop le')