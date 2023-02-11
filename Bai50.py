def so_Nguyen_To(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    i = 2
    for i in range(2, n, 1):
        if n % i == 0:
            break
    if i == n - 1:
        return True
    else:
        return False
a, b = map(int, input().rstrip('').split())
if a > b:
    print('a > b')
elif a < 0 or b < 0:
    print('a < b')
else:
    for i in range(a, b + 1, 1):
        if so_Nguyen_To(i) == True:
            print(i, end= ' ')
