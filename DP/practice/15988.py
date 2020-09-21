# 정수 4를 1,2,3의 합으로 나타내는 방법. 1개 이상의 수 사용

# 점화식 D[n] = D[n-1] + D[n-2] + D[n-3]
import sys
loop = int(sys.stdin.readline())
mod = 1000000009
DP = [0] * 1000001
DP[1] = 1
DP[2] = 2
DP[3] = 4
lst = []
for i in range(loop):
    lst.append(int(sys.stdin.readline()))

for j in range(4, max(lst)+1):
    DP[j] = DP[j-1] % mod + DP[j-2] % mod + DP[j-3] % mod

for el in lst:
    print(DP[el]&mod)

