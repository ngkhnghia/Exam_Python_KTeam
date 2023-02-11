try:
    n = int(input())
    if n < 0:
        print('vui long nhp n > 0')
    else:
        char = 65
        for i in range(1, n + 1, 1):
            for j in range(1, 2*n, 1):   
                if j in range(n - i + 1, n + i, 1):
                    print(chr(char), end= '')
                    char += 1
                    if char > 90:
                        char = 65
                else:
                    print(' ', end= '')
            print('')
except:
    print('dinh dang dau vao khong hop le')