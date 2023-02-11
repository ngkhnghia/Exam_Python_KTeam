try:
    var1 = input().rstrip(' ').split()
    var2 = input().rstrip(' ').split()
    name1 = str(var1[0])
    age1 = int(var1[1])
    name2 = str(var2[0])
    age2 = int(var2[1])
    if age1 < age2:
        print(name2)
    else:
        print(name1)
    pass
except:
    print('dinh dang dau vao khong hop le')