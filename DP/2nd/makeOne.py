num = int(input())

DP = []
cnt = 0


while True:
    print(DP)
    if not DP:
        temp = []
        if num % 5 == 0:
            temp.append(num // 5)
        if num % 3 == 0:
            temp.append(num // 3)
        if num % 2 == 0:
            temp.append(num // 2)
        temp.append(num-1)
        DP.append(temp)
    else:
        temp = []
        if 1 in DP[-1]:
            break
        for el in DP[-1]:
            if el % 5 == 0:
                temp.append(el // 5)
            if el % 3 == 0:
                temp.append(el // 3)
            if el % 2 == 0:
                temp.append(el // 2)
            temp.append(el-1)
        DP.append(temp)
    cnt +=1

print(cnt)



