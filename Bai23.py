from cmath import sqrt
with open('fin_bai23.txt', 'r') as f:
    line1 = f.readline().rstrip('\n').rsplit()
    line2 = f.readline().rstrip('\n').rsplit()
if line1 == ['1']:
    print('giai phuong trinh bac nhat')
    a, b = map(float, line2)
    if a == 0:
        if b == 0:
            thongBao = 'phuong trinh co vo so nghiem'
        else:
            thongBao = "phuong trinh vo nghiem"
    else:
        thongBao = 'phuong trinh co nghiem duy nhat x = {}'.format(-b/a)
elif line1 == ['2']:
    thongBao = 'giai phuong trinh bac 2'
    a, b, c = map(float, line2)
    if a == 0:
        if b == 0:
            if c == 0:
                thongBao = 'phuong trinh vo so nghiem'
            else:
                thongBao = 'phuong trinh vo nghiem'
        else:
            thongBao = 'phuong trinh co nghiem duy nhat x = {}'.format(-c/b)
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            thongBao = 'phuong trinh vo nghiem'
        elif delta == 0:
            thongBao = 'phuong trinh co nghiem kep x1 = x2 = {}'.format(-b/(2*a))
        else:
            thongBao = 'phuong trinh co 2 nghiem phan biet x1 = {}, x2 = {}'.format((-b + sqrt(delta)) / (2*a), (-b -sqrt(delta) / (2*a)))
with open('fout_bai23.txt', 'w') as f:
    f.write(thongBao)