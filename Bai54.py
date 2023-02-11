def kiem_Tra(s1, s2):
    if s2 in s1:
        print(s1.count(s2))
    else:
        print('{} khong nam trong {}'.format(s2, s1))
s1 = input()
s2 = input()
kiem_Tra(s1, s2)