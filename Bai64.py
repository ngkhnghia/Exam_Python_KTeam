def xoa_Tu_Trung(s):
    temp = ''
    for i in s:
        if i not in temp:
            temp += i
    return temp
s = input()
print(xoa_Tu_Trung(s))