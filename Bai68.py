def so_Lan_Xuat_Hien(s):
    temp = ''
    for i in s:
        if i not in temp:
            temp += i
    for i in temp:
        print('{}: {}'.format(i, s.count(i)), end= '; ')
s = input()
so_Lan_Xuat_Hien(s)