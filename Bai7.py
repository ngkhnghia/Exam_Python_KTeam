a = (input())
b = (input())
try:
    a = float(a)
    b = int(b)
    print('{0:.{1}f}'.format(a, b))
except:
    print("dinh dang dau vao khong hop le!")