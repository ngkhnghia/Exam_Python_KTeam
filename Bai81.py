def danhSachPhanTuXuatHienDuyNhat(s):
    result = []
    for phanTu in s:
        if s.count(phanTu) == 1:
            result.append(phanTu)
    return result
s = input().split()
print(*danhSachPhanTuXuatHienDuyNhat(s))
