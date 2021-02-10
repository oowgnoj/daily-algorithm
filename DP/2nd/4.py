n = int(input())
lst = list(map(int, input().split(' ')))

DP = [1] * n
# LIS 문제랑 똑같다
# LIS 어떻게 풀었더라


for i in range(1, n):
    DP[i] = DP[i-1]
    if lst[i] < lst[i-1]:
        DP[i] = DP[i-1] + 1

print(n-max(DP))

DP2 = [1] * n

# LIS 문제랑 똑같다
# LIS 어떻게 풀었더라


for i in range(1, n):
    for j in range(0, i):
        if lst[i] < lst[j] and DP2[i] < DP2[j]+1:
            DP2[i] = DP2[j] + 1

print(n-max(DP2))