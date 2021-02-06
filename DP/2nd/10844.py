import sys
import copy
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split(' ') )) 

DP = [[[lst[0], 1]], []]
for i in range(1, n):
    temp = DP[0]
    for j in range(len(DP[0])):
        largest, num = DP[0][j]
        # i 번째 값이 기존 수열의 마지막 값보다 클 때
        if lst[i] > largest:
            temp[j][0] = lst[i]
            temp[j][1] = num+1
        # i 번째 값이 기존 수열의 마지막 값보다 작을 때
        elif lst[i] < largest:
            x = [_[0] for _ in DP[0] if _[0] < largest]
            if not x:
                temp.append([lst[i], 1])
        
        elif lst[i] == largest:
            continue
    # print(temp)
    DP[0] = temp
# print(DP)
print(max([_[1] for _ in DP[0]]))



