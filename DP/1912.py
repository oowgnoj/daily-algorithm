# n 개의 수열이 주어졌을때, 연속된 한개 이상의 수를 더한 가장 큰 합이 무엇인가?
# 10
# 10 -4 3 1 5 6 -35 12 21 -1

# 5
# -1 -2 -3 -4 -5


# 풀이
# max_num = -1000
# D[n] = max(D[n-1], D[n-1]+ n)
# D[n] = max(D[n], D[n-1]+ n)


# 시간초과 -> O(N2)에다가 계산해뒀던 것을 쓰지 않았음
# num = int(input())
# lst = list(map(int, str(input()).split(' ')))
# DP = [0] * (num)
# for i in range(num):
#     DP[i] = lst[i]
#     flag = False
#     for j in range(i, num):
#         if DP[i] < sum(lst[i:j]):
#             DP[i] = sum(lst[i:j])
#             flag = True
#         elif flag:
#             break
        
# print(max(DP))


# num = int(input())
# lst = list(map(int, str(input()).split(' ')))
# sum = [lst[0]]
# for i in range(num-1):
#     sum.append(max(sum[i] + lst[i+1], lst[i+1]))

# print(max(sum))

n = int(input())
a = list(map(int, input().split()))
sum = [a[0]]
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print(sum)
print(max(sum))