def xoa_Phan_Tu(s):
    s_Le = ''
    s_Chan = ''
    for i in range(len(s)):
        if i % 2 == 0:
            s_Le += s[i]
        else:
            s_Chan += s[i]
    if len(s) % 2 == 0:
        return s_Le
    else:
        return s_Chan
s = input()
print(xoa_Phan_Tu(s))