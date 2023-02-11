inp = tuple(map(float, input().split()))
if len(inp) == 0:
    print("Danh sach rong")
else:
    print(max(inp))
    print(min(inp))
    print(len(inp))