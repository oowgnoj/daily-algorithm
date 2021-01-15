N = int(input())
dis = list(map(int, input().split(' ')))
prices = list(map(int, input().split(' ')))

ans = 0
P = prices[0]
D = dis[0]
for i in range(1, len(prices)-1):
    if prices[i] < P:
        ans += D * P
        P = prices[i]
        D = dis[i]
    else:
        D += dis[i]
if D:
    ans += P * D
print(ans)
