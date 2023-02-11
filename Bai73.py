def kyTuDaoNguoc(s):
    s = list(s)
    s = s[::-1]
    return s
s = input()
print(*kyTuDaoNguoc(s))