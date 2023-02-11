def ky_Tu_Va_So(s):
    s = s.strip().split()
    count = 0
    for tu in s:
        digit = 0
        alpha = 0
        for i in tu:
            if i.isdigit():
                digit = 1
            if i.isalpha():
                alpha = 1
        if digit == 1 and alpha == 1:
            count += 1
    return count
s = input()
print(ky_Tu_Va_So(s))