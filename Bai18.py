num1, phepTinh, num2 = input().split()
num1 = float(num1)
num2 = float(num2)
if phepTinh == '+':
    print("{} {} {} = ".format(num1, phepTinh, num2), num1 + num2)
elif phepTinh == '-':
    print("{} {} {} = ".format(num1, phepTinh, num2), num1 - num2)
elif phepTinh == '*':
    print("{} {} {} = ".format(num1, phepTinh, num2), num1 * num2)
elif phepTinh == '/':
    if num2 == 0:
        print("So chia phai khac 0!")
    else: 
        print("{} {} {} = ".format(num1, phepTinh, num2), num1 / num2)