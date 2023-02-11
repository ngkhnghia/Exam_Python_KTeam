def so_Hoan_Thien(n):
    sum = 0
    for i in range(1, n, 1):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False
def hien_Day_So_Hoan_Thien(n):
    for i in range(n):
        if so_Hoan_Thien(i):
            print(i, end= ' ')
n = int(input())
if n < 0:
    print('n > 0')
else:
    hien_Day_So_Hoan_Thien(n)