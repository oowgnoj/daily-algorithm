n = int(input())
lst = [0] + [int(input()) for _ in range(n)]
DP = [0] * (n+1)
for i in range(1, n+1):
    if i <= 2:
        DP[i] = sum(lst[:i+1])

    elif i == 3:
        DP[i]=max(lst[1]+lst[2], lst[1]+lst[3], lst[2]+lst[3])
        continue
    else:
        a = lst[i] + lst[i-1] + DP[i-3]
        b = lst[i] + DP[i-2]
        c = DP[i-1]
        DP[i] = max(a,b,c)
    

# print(DP)
print(DP[n])