def ky_Tu_Nguyen_Am(s):
    list_Nguyen_Am = ['u', 'e', 'o', 'a', 'i', 'U', 'E', 'O', 'A', 'I']
    count = 0
    for i in list_Nguyen_Am:
        if i in s:
            count += s.count(i)
            s = s.replace(i, '$')
    return count, s
s = input()
print(ky_Tu_Nguyen_Am(s)[0], '\n',ky_Tu_Nguyen_Am(s)[1])