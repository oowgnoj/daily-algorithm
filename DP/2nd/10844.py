mod = 1000000000
num = int(input())
DP = [[0,0,0,0,0,0,0,0,0,0] for _ in range(101)]
DP[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2, num+1):
    for j in range(10):
        if j == 0:
            DP[i][j] = DP[i-1][j+1] % mod 
        elif j ==9:
            DP[i][j] = DP[i-1][j-1] % mod   
        else:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1] % mod

print(sum(DP[num])%mod)