def xoa_Khoang_Trang(s):
    s = s.strip(' ')
    while True:
        if '  ' in s:
            s = s.replace('  ', ' ')
        else:
            break
    return s
s = input()
print(xoa_Khoang_Trang(s))