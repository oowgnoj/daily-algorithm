# 가장 긴 증가하는 부분수열 + 수열 리턴
# 예를 들어, 
# 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 
# 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

num = int(input())
lst = list(map(int, str(input()).split(' ')))
lst = [0] + lst
DP = [1] * (num + 1)
DP[0] = 0
maxNum = 0
sec = []
for i in range(1, num+1):
    for j in range(i-1, 0, -1):
        if lst[i] > lst[j]:
            if DP[j] + 1 > DP[i]:
                DP[i] = DP[j] + 1

order= max(DP)
for i in range(num, 0, -1):
    if DP[i]==order:
        sec.append(lst[i])
        order-=1
sec.reverse()

for i in sec:
    print(i, end=' ')

