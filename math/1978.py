# 소수 구하기

loop = int(input())
lst = list(map(int, str(input()).split(' ')))


num = 0
for i in range(loop):
    if lst[i] == 1:
        continue
    isTrue = True
    for j in range(2, lst[i]):
        if lst[i] % j == 0 :
            isTrue = False
    if isTrue:
        num +=1
        

print(num)