def cong(a, b):
    return a + b
def tru(a, b):
    return a - b
def nhan(a, b):
    return a * b
def chia(a, b):
    if b == 0:
        print('b phai khac 0')
    else:
        return a / b
def may_Tinh(a, phep_Tinh, b):
    if phep_Tinh == '+':
        return cong(a, b)
    elif phep_Tinh == '-':
        return tru(a, b)
    elif phep_Tinh == '*':
        return nhan(a, b)
    elif phep_Tinh == '/':
        return chia(a, b)
a, phep_Tinh, b = input().rstrip(' ').rsplit()
a = float(a)
b = float(b)
print(may_Tinh(a, phep_Tinh, b))