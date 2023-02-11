a, b, c = map(float, input().split())
if a + b > c and a + c > b and b + c > a:
    print("{}, {}, {} la 3 canh cua mot tam giac".format(a, b, c))
else:
    print("{}, {}, {} khong la 3 canh cua mot tam giac".format(a, b, c)) 