def bien_Doi_Chuoi(s):
    if s[0].isupper():
        return s.upper()
    if s[0].islower():
        return s.lower()
    return s
s = input()
print(bien_Doi_Chuoi(s))