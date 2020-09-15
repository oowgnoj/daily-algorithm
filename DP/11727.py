# D[n] = 2*n을 채우는 방법의 수

num = int(input())
memo = []
memo.append(1)
memo.append(1)
memo.append(3)

for i in range(3, num +1):
    a = memo[i -1] + memo[i-2] + memo[i-2]
    memo.append(a)

ans= memo[-1] % 10007
print(ans)

