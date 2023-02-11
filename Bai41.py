try:
    name = input()
    age = int(input())
    if age < 1:
        print('tuoi phai > 0')
    else:
        print('Xin chap! Toi la {}, toi {} tuoi'.format(name, age))
    pass
except:
    print('dinh dang dau vao khong hop le')