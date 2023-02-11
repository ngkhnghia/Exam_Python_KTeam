ls = input()
ls = ls.split()
try:
    ls = map(int, ls)
    sum = sum(ls)
    print(sum)
except:
    print("dinh dang dau vao khong hop le!")
