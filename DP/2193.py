# 이친수
# D[n] = D[n-1][1] + D[n-1][0]
# 0 -> 0 또는 1
# 1 -> 0
DP = [[0,0] for _ in range(91)]
num = int(input())
ans = [0,1,1,2] 

DP[2] = [1,0]
DP[3] = [1,1]

for i in range(4, num+1):
    DP[i][0] = DP[i-1][0] + DP[i-1][1]
    DP[i][1] = DP[i-1][0] 
    ans.append(sum(DP[i]))
print(ans[num])

