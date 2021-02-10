n = int(input())
lst = [(0,0,0)]
for _ in range(n):
    lst.append(tuple(map(int, input().split(' '))))

DP = [[]]
for i in range(1,n+1):
    if i == 1:
        DP.append(lst[1])
    else:
        temp=[0,0,0]
        temp[0] = lst[i][0] + min(DP[i-1][1], DP[i-1][2])
        temp[1] = lst[i][1] + min(DP[i-1][0], DP[i-1][2])
        temp[2] = lst[i][2] + min(DP[i-1][1], DP[i-1][0])
        DP.append(temp)

        

print(min(DP[n]))
