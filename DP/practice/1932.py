num = int(input())
lst = [[0]]
DP = [[0]]
for i in range(num):
    lst.append(list(map(int, str(input()).split(' '))))
    DP.append([0]*(i+1))

DP[0] = lst[0]

for i in range(1, num + 1):
    for j in range(len(lst[i])):
        if j == 0:
            DP[i][j] = DP[i-1][j] + lst[i][j]
        elif j == len(lst[i])-1:
            DP[i][j] = DP[i-1][j-1] + lst[i][j]
        else:
            DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + lst[i][j]

print(max(DP[num]))
