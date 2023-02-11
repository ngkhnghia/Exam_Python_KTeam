def nhanHaiDanhSach(a, b):
    result = [so1 * so2 for so1, so2 in zip(a, b[::-1])]
    return result

list1 = input().split()
list2 = input().split()
if len(list1) != len(list2):
    print("Do dai 2 danh sach khong bang nhau")
else:
    try:
        list1 = list(map(float, list1))
        list2 = list(map(float, list2))
        print(*nhanHaiDanhSach(list1, list2))
    except:
        print("Danh sach co phan tu khong la so thuc")