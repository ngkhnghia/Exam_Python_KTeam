try:
    with open('fin_bai22.txt', 'r') as f:
        data = f.read()
    arr = ['', '', '']
    count = 0
    for i in range(len(arr)):
        while count < len(data):
            if data[count] != " ":
                arr[i] += data[count]
                count += 1
            else:
                count += 1
                break
    a, b, c = map(float, arr)
    if a > 0 and b > 0 and c > 0:
        if a + b > c and b + c > a and c + a > b:
            if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
                loai = 'vuong'
                thongBao = "{}, {}, {} la 3 canh cua tam giac {}".format(a, b, c, loai)
            elif a == b != c or b == c != a or c == a != b:
                loai = 'can'
                thongBao = "{}, {}, {} la 3 canh cua tam giac {}".format(a, b, c, loai)
            elif a == b == c:
                loai = 'deu'
                thongBao = "{}, {}, {} la 3 canh cua tam giac {}".format(a, b, c, loai)
            elif a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or c**2 + a**2 < b**2:
                loai = 'tu'
                thongBao = "{}, {}, {} la 3 canh cua tam giac {}".format(a, b, c, loai)
            else:
                loai = 'nhon'
                thongBao = "{}, {}, {} la 3 canh cua tam giac {}".format(a, b, c, loai)
        else:
            thongBao = "{}, {}, {} la 3 canh cua tam giac {}".format(a, b, c)
    else:
        thongBao = "{}, {}, {} la 3 canh cua tam giac {}".format(a, b, c)
except FileNotFoundError:
    thongBao = print("khong tim duoc file!")
except:
    thongBao = "dinh dang dau vao khong hop le!"
with open('fout_bai22.txt', 'w') as f:
    f.write(thongBao)