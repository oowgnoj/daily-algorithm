
num = int(input())
lst = list(map(int, str(input()).split(' ')))

DP = [0 for _ in range(num)]
for i in range(num):
    DP[i] =1
    for j in range(i):
        if lst[i] > lst[j] and DP[i] < DP[j]+1:
            DP[i] = DP[j] +1

print(max(DP))