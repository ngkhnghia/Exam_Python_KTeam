def fib(n) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
try:
    n = int(input())
    if n <= 0:
        print('n > 0')
    else:
        if n == 1 or n == 2:
            print(1)
        else:
            print(fib(n))
except:
    print('dinh dang dau vao khong hop le')