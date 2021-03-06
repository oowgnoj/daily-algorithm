# 각 집을 빨강, 초록, 파랑으로 칠해야 한다. 
# 이 때 n 번째 집의 색은 n-1, n+1 의 집의 색과 동일하면 안된다
# 각 집을 칠하는데 최소값을 구하라

# 입력 예시
# 3
# 26 40 83
# 49 60 57
# 13 89 99



# D[n] = D[n-1]까지의 최솟값 + min(D[n]을 빨강, 초록, 파랑중에 선택)
# 전 값이 R인지, G 인지, B 인지 알아야 한다.

# 점화식 : D[n] = D[n-1] + min(빨강, 초록, 파랑 except n-1)

import sys
loop = int(sys.stdin.readline())
DP = [[0,0,0] for _ in range(1001)]
 
lst = [[0,0,0]]
ans = []
for i in range(1,loop+1):
    lst.append(list(map(int, str(input()).split(' '))))


for i in range(1, loop+1):
    DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + lst[i][0]
    DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + lst[i][1]
    DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + lst[i][2]
    ans.append(min(DP[i]))
print(ans[-1])
