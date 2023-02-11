try:
    n = int(input())
    if n < 0:
        print('n >= 0')
    else:
        sum_Odd = 0
        sum_Eve = 0
        while n > 0:
            i = int(n % 10)
            if i % 2 == 0:
                sum_Eve += i
            else:
                sum_Odd += i
            n = int(n / 10) 
        print(sum_Odd * sum_Eve)
except:
    print('dinh dang dau vao khong hop le')