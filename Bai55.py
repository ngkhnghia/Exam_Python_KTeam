def dao_Nguoc(s, a, b):
    s1 = s[:a]
    s2 = s[a:b + 1]
    s2 = s2[::-1]
    s3 = s[b+1:]
    s = s1 + s2 + s3
    return s
s = input()
a, b = map(int, input().rstrip(' ').split())
print(dao_Nguoc(s, a, b))