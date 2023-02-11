def tu_Dai_Nhat(s):
    s = s.split()
    max = 0
    temp = ''
    for i in s:
        if len(i) > max:
            temp = i
        elif len(i) == max and i < temp:
            temp = i
    return temp
s = input()
print(tu_Dai_Nhat(s))