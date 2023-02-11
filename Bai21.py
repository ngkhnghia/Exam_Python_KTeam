a, b, c = map(float, input().split())
if a + b > c and b + c > a and c + a > b:
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        loai = 'vuong'
        print("{}, {}, {} la 3 canh cua tam giac {}".format(a, b, c, loai))
    elif a == b != c or b == c != a or c == a != b:
        loai = 'can'
        print("{}, {}, {} la 3 canh cua tam giac {}".format(a, b, c, loai))
    elif a == b == c:
        loai = 'deu'
        print("{}, {}, {} la 3 canh cua tam giac {}".format(a, b, c, loai))
    elif a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or c**2 + a**2 < b**2:
        loai = 'tu'
        print("{}, {}, {} la 3 canh cua tam giac {}".format(a, b, c, loai))
    else:
        loai = 'nhon'
        print("{}, {}, {} la 3 canh cua tam giac {}".format(a, b, c, loai))
else:
    print("{}, {}, {} khong phai la canh mot tam giac".format(a, b, c))