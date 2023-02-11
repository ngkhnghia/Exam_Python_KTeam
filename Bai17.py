a, b, c = map(float, input().split())
try:
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            print("{}, {}, {} la 3 canh cua mot tam giac".format(a, b, c))
        else:
            print("{}, {}, {} khong la 3 canh cua mot tam giac".format(a, b, c))
    else:
        print("3 canh cua tam giac phai lon hon 0!a")
except:
    print("dinh dang dau vao khong hop le!")