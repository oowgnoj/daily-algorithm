# 4
# 1 5 6 7

# 카드 4개를 사고자 할 때 아래 카드의 조합 중 최대값을 구해라
# n = 카드 n개를 구매했을 때 최대값

# 1 -> 1
# 2 -> max((n -1) + (n -1), n)
# 3 -> max() 

num = int(input())
lst = list(map(int, str(input()).split(' ')))

memo = []
memo.append(0)
memo.append(lst[0])
memo.append(max(lst[0] * 2, lst[1]))
for i in range(3, num + 1):
    memo.append(max(i * lst[0], lst[i-1]))
    for j in range(1, i+1):
        temp = memo[j] + memo[i -j]
        if(memo[i] < temp):
            memo[i] = temp

print(memo[-1])
