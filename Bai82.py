from unittest import result


def dsLapLai(s, n):
    s = s + ' '
    s_ = s * n
    s_ = s_.split()
    result = []
    for i in range(n):
        result.append(s_[i])
    return result
s = input()
n = int(input())
print(*dsLapLai(s, n))