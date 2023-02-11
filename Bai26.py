try:
    a = int(input())
    b = int(input())
    sum = 0
    if a > b:
        print('a > b')
    else:
        i = a
        while i <= b:
            sum += i
            i += 1
        print(sum)
except:
    print('dinh dang dau vao khong hop le!')