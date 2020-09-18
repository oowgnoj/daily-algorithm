# 가장 긴 증가하는 부분수열
# 예를 들어, 
# 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 
# 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

num = int(input())
lst = list(map(int, str(input()).split(' ')))
lst = [0] + lst
DP = [1] * (num + 1)

for i in range(1, num+1):
    for j in range(i-1, 0, -1):
        if lst[i] > lst[j] and DP[j] + 1 > DP[i] :
            if DP[j] + 1 > DP[i]:
                DP[i] = DP[j] + 1

print(max(DP))


