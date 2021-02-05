n = int(input())
lst = [int(input()) for _ in range(n)]
DP = [0] * n


for i in range(min(2,n)):
    DP[i] = sum(lst[:i+1]) 



for i in range(2, n):
    if i == 2:
        DP[i] = max(lst[i-2] + lst[i], lst[i-1] + lst[i])
    else:
        a = DP[i-2] + lst[i] 
        b = lst[i-1] + lst[i]+ DP[i-3]
        DP[i] = max(a,b)

print(DP[n-1])