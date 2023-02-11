def themPhanTu(s, n):
    for i in range(len(s)):
        if s[i] % n == 0:
            s[i] = 'Kteam'
            i += 1
    return s
s = list(map(int, input().split()))
n = int(input())
print(*themPhanTu(s, n))