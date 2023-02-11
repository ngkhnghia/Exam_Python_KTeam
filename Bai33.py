try:
    x = float(input())
    n = int(input())
    if n < 0:
        print('n > 0')
    elif n == 0:
        print('1')
    else:
        sum = 0
        gt = 1
        for i in range(1, 2*n  + 1, 1):
            gt = gt*i
            sum += (-1)**(i - 1)*x**i/gt
        print('{:.5f}'.format(sum))
except:
    print('dinh dang dau vao khong hop le')