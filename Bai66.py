def xoa_Space(s):
    s = s.strip()
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s
def hien_Cau(s):
    list_Cau = s.split('.')
    for cau in list_Cau:
        print(xoa_Space(cau).title())
s = input()
hien_Cau(s)