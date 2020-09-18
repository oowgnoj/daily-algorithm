# 제곱수의 합 (1699)

# D[n] = i보다 작은 수 중 j^2이 i보다 작은 수 + DP[i-j^2]

import sys
num = int(sys.stdin.readline())
DP = [0] * (num+1)
for i in range(1, num+1):
    DP[i] = i
    for j in range(1,i):
        if(j * j > i):
            break
        if DP[i] > DP[i-j*j]+1:
            DP[i] = DP[i-j*j] + 1
print(DP[-1])


