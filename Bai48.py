def giai_Thua(n):
    if n == 0:
        return 1
    else:
        return n * giai_Thua(n - 1)
n = int(input())
if n < 0:
    print('n > 0')
else:
    print(giai_Thua(n))
