def doi_Chuoi(s):
    if s[len(s) - 3: len(s) + 1: 1] == 'ing':
        s = s[:len(s) - 3: 1]
        s += 'ly'
    else:
        s += 'ing'
    return s
s = input()
print(doi_Chuoi(s))