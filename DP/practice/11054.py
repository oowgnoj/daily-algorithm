num = int(input())
lst = list(map(int, str(input()).split(' ')))
lst = [0] + lst
DP = [0 for _ in range(num+1)]
DP2 = [1 for _ in range(num+1)]


for i in range(1, num+1):
    temp = 0
    for j in range(i):
        if lst[i] > lst[j] and temp <= DP[j]:
            temp = DP[j]+1
    DP[i]= temp

for i in range(num, 0, -1):
    temp = 1
    for j in range(i+1, num+1):
        if lst[i] > lst[j] and DP2[j]+1 > temp:
            temp = DP2[j]+1
    DP2[i]= temp

max_num = 0
for i in range(1, len(DP)):
    if DP[i] and DP2[i]:
        if DP[i]+ DP2[i] > max_num:
            max_num= DP[i] + DP2[i] - 1
    else:
        if max_num < max(DP[i], DP2[i]):
            max_num = max(DP[i], DP2[i])
print(max_num)
