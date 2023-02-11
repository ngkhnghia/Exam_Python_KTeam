def tachDanhSach(inp):
    tbc = sum(inp) / len(inp)
    listLonHon = [i for i in inp if i >= tbc]
    listNhoHon = [i for i in inp if i < tbc]
    return tbc, listNhoHon, listLonHon

try:
    inp = list(map(float, input().split()))
    tbc, listNhoHon, listLonHon = tachDanhSach(inp)
    print(tbc)
    print(*listNhoHon)
    print(*listLonHon)
except:
    print("Danh sach co phan tu khong phai so thuc")
