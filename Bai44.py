def de_Quy(n):
    if n == 0:
        return 0
    else:
        return (n + de_Quy(n - 1))
n = int(input())
print(de_Quy(n))