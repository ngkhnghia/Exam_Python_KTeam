try:
    a = int(input())
    b = int(input())
    if a > b:
        print('a > b')
    else:
        count = 0
        for i in range(a, b + 1, 1):
            if i == b:
                print('\nda in het cac so chia het cho 5')
            if i % 5 == 0 and count <= 10:
                count += 1
                print(i, end= " ")
            elif count > 10:
                print('\nda in 10 so roi')
                break
    pass
except:
    print('dinh dang dau vao khong hop le!')