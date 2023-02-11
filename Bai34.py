try:
    n = int(input())
    if n < 0:
        print('n >= 0')
    else:
        while n > 0:
            print(int(n%10), end= '')
            n = int(n / 10)
except:
    print('dinh dang dau vao khong hop le')