# 쉬운 계단수
# 45656이란 수를 보자.
# 이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.
# 세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. 
# (0으로 시작하는 수는 없다.)

# 1 <= n < 100
# 점화식 D[n] = D[n-1] +
# 점화식 D[n] = D[n-1][] + D[n-1][0] + D[n-1][2] + D[n-][2] + D[n-][]

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


# note
# DP 는 점화식이 중요하다. 