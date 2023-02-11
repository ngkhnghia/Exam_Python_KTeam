try:
    n = int(input())
    if n >= 0:
        if n == 0:
            print('1')
        else:
            gt = 1
            for i in range(1, n + 1, 1):
                gt *= i
            print(gt)
    else:
        print('n > 0')
except:
    print('dinh dang dau vao khong hop le')