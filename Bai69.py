def xu_Ly_Chuoi(s):
    list_S = s.rstrip().split()
    sum = 0
    count = 0
    for chuoi in list_S:
        if chuoi.isdigit():
            sum += float(chuoi)
            count += 1
    print(sum)
    print(sum / count)
s = input()
xu_Ly_Chuoi(s)