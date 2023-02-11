def mul(tong_Chan, tong_Le):
    return tong_Chan * tong_Le
def phan_Loai(n):
    tong_Chan = 0
    tong_Le = 0
    while n > 0:
        if n % 2 == 0:
            tong_Chan += n % 10
            n = int(n / 10)
        else:
            tong_Le += n % 10
            n = int(n / 10)
    print(mul(tong_Chan, tong_Le))
n = int(input())
if n < 0:
    print('Loi')
else:
    phan_Loai(n)
