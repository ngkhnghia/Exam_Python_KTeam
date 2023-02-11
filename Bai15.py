try:
    name1, cCao1 = input().split()
    name2, cCao2 = input().split()
    cCao1 = int(cCao1)
    cCao2 = int(cCao2)
    if cCao1 <= 0 or cCao2 <= 0:
        print('chieu cao phai lon hon 0!')
    else:
        if cCao1 > cCao2:
            print(name1 + ' cao hon ' + name2)
        elif cCao1 < cCao2:
            print(name2 + ' cao hon ' + name1)
        else:
            print(name1 + ' cao bang ' + name2)
except:
    print('dinh dang dau vao khong hop le!')