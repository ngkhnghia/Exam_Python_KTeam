def lietKe(s):
    s = s.split(' ')
    s = enumerate(s, 0)
    for key, value in s:
        print(key, value)
s = input()
lietKe(s)