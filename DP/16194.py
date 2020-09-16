
# DP 점화식 적용
num = int(input())
lst = list(map(int, str(input()).split(' ')))
lst = [0] + lst
memo = [0] + [-1] * (num)
for i in range(1, num + 1):
    for j in range(1, i+1):
        if memo[i] == -1:
            memo[i] = memo[i-j] + lst[j]
        elif memo[i] > memo[i-j] + lst[j]:
            memo[i] = memo[i-j] + lst[j]
print(memo[-1])