# DP
# 무엇을 저장할 것인가?

n = int(input())
lst = list(map(int, input().split(' ')))

DP = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if lst[i] >lst[j]:
            if DP[j] + 1 > DP[i]:
                DP[i] = DP[j]+1
    
    

# print(DP)
print(max(DP))