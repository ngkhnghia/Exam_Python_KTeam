try:
    a = int(input())
    b = int(input())
    sum = 0
    if a > b:
        print('a > b')
    else:
        for i in range(a, b + 1, 1):
            sum = sum + i
        print(sum)
except:
    print('dinh dang dau vao khong hop le!')