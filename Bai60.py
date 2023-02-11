def chuyen_Hoa_Thuong(s):
    if s.startswith('*') and s.endswith('*') or s.startswith('-') and s.endswith('-'):
        return s.title()
    else:
        return s.capitalize()
s = input()
print(chuyen_Hoa_Thuong(s))