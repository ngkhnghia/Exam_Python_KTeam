def xoaKhoangTrang(s):
    for i in range(len(s)):
        while '  ' in s[i]:
            s[i] = s[i].replace('  ', ' ')
        s[i] = s[i].strip()
    return s
def noiTenVoiQuocTich(dsTen, dsQuocTich):
    dsTen = xoaKhoangTrang(dsTen)
    dsQuocTich = xoaKhoangTrang(dsQuocTich)
    dsZip = set(zip(dsTen, dsQuocTich))
    return dsZip
dsTen = input().split(',')
dsQuocTich = input().split(',')
print(*noiTenVoiQuocTich(dsTen, dsQuocTich))
