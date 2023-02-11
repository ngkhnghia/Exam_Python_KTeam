try:
    a = int(input())
    b = int(input())
    if a < 0 or b < 0:
        print('a, b >= 0')
    else:
        if a > b:
            print('a < b')
        else:
            for i in range(a, b + 1, 1):
                if i == 0 or i == 1:
                    continue
                elif i == 2:
                    print(2, end= ' ')
                else:
                    j = 2
                    for j in range(2, i, 1):
                        if i % j == 0 and j < i:
                            break
                    if j == i - 1:
                        print(i, end= ' ')
except:
    print('dinh dang dau vao khong hop le')