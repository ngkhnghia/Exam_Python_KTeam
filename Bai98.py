inp = tuple(input().split())
value = input()
index = tuple(i for i in range(len(inp)) if inp[i] == value)
print(index)