def count_0(data):
    countNumber = 0
    countCharacter = 0
    for i in range(len(data)):
        if type(data[i]) == int or type(data[i]) == float:
            if data[i] == 0:
                countNumber += 1
        if type(data[i]) == str:
            for j in range(len(data[i])):
                if '0' == data[i][j]:
                    countCharacter += 1
    return (countNumber, countCharacter)


data = (0, '00', 0000, " haha ", False)
print(*count_0(data))