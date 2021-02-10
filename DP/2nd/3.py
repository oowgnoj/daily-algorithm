n = int(input())
lst = [0] + [list(map(int, input().split(' '))) for _ in range(min(n,16))]

DP = [0] * (16)

for i in range(1, n+1):
    after, payment = lst[i]
    DP[i] = DP[i-1]
    if after == 1:
        DP[i] = DP[i-1] + payment
    
    for j in range(1, i):


        
        if lst[j][0]-1 + j == i:
            if DP[i] != DP[j]:
                DP[i] = max(DP[i], lst[j][1] + DP[j])
            else:
                DP[i] = max(DP[i], DP[j-1] + lst[j][1])

# print(lst)
# print(DP)
print(DP[n])
