# D[n] = 2*n을 채우는 방법의 수

num = int(input())
memo = []
memo.append(1)
memo.append(1)
memo.append(2)
if num < 3:
    print(memo[num] % 10007)
else:
    for i in range(3, num +1):
        temp = memo[i -1] + memo[i-2]
        memo.append(temp)

    ans = memo[-1] % 10007
    print(ans)

