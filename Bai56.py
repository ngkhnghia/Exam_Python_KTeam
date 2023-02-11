def dan_Xen(s1, s2):
    s = ''
    s2 = s2[::-1]
    for i in range(max(len(s1), len(s2))):
        if i < len(s1):
            s += s1[i]
        if i < len(s2):
            s += s2[i]
    return s
s1 = input()
s2 = input()
print(dan_Xen(s1, s2))