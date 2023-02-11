from cmath import sqrt


def bac_Nhat(a, b):
    if a == 0:
        if b == 0:
            print('phuong trinh vo so nghiem')
        else:
            print('phuong trinh vo nghiem')
    else:
        print('phuong trinh co nghiem duy nhat x = {}'.format(-b / a))
def bac_Hai(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print('phuong trinh vo so nghiem')
            else:
                print('phuong trinh vo nghiem')
        else:
            print('phuong trinh co nghiem duy nhat x = {}'.format(-c / b))
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print('phuong trinh vo nghiem')
        elif delta == 0:
            print('phuong trinh co nghiem kep x1 = x2 = {}'.format(-b / (2*a)))
        else:
            print('phuong trinh co 2 nghiem phan biet x1 = {}, x2 = {}'.format((-b + sqrt(delta) / (2*a)), (-b - sqrt(delta) / (2*a))))
chuc_Nang = int(input())
if chuc_Nang == 1:
    a, b = map(float, input().rstrip('').rsplit())
    bac_Nhat(a, b)
elif chuc_Nang == 2:
    a, b, c = map(float, input().rstrip('').rsplit())
    bac_Hai(a, b, c)
else:
    print('chon 1 hoac 2')
