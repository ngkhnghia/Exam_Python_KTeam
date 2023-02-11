def xoa_Khoang_Trang(s):
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s
def can_Giua(s, max_Length):
    s = s.center(max_Length, ' ')
    return s
def hien_Thi(s):
    s = xoa_Khoang_Trang(s)
    s = s.strip().split('.')
    max_Length = 0
    for cau in s:
        if len(cau) > max_Length:
            max_Length = len(cau)
    for cau in s:
        print(can_Giua(cau, max_Length))
s = input()
hien_Thi(s)