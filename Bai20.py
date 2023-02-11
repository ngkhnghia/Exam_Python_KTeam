try:
    from cmath import sqrt
    a, b, c = map(float, input().split())
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phuong trinh co vo so nghiem!")
            else:
                print("Phuong trinh vo nghiem!")
        else:
            print("Phuong trinh co nghiem duy nhat: x = {}".format(float(-c/b)))
    else:
        delta = float(b**2 - 4*a*c)
        if delta < 0:
            print("Phuong trinh vo nghiem!")
        elif delta == 0:
            print("Phuong trinh co nghiem kep: x1 = x2 = {}".format(float(-b/2*a)))
        else:
            print("Phuong trinh co 2 nghiem phan biet: x1 = {}, \tx2 = {}".format(float((-b + sqrt(delta)) / (2*a)), float((-b - sqrt(delta)) / (2*a))))
except:
    print("dinh dang dau vao khong hop le!")