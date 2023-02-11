def xu_Ly_Ky_Tu(s):
    chu_so = ''
    dem_Chu_So = 0
    ky_Tu = ''
    dem_Ky_Tu = 0
    ky_Hieu = ''
    dem_Ky_Hieu = 0
    temp = ''
    for i in s:
        if i.isdigit():
            chu_so += i
            dem_Chu_So += 1
        elif i.isalpha():
            ky_Tu += i
            dem_Ky_Tu += 1
        else:
            ky_Hieu += i
            dem_Ky_Hieu +=1
    print(dem_Chu_So)
    print(dem_Ky_Tu)
    print(dem_Ky_Hieu)
    print(chu_so + ky_Tu + ky_Hieu)
s = input()
xu_Ly_Ky_Tu(s)