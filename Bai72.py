def soVaBinhPhuong(n):
    listSo = [x for x in range(n)]
    listBinhPhuong = [x**2 for x in range(n)]
    return listSo, listBinhPhuong
n = int(input())
print(soVaBinhPhuong(n)[0])
print(soVaBinhPhuong(n)[1])