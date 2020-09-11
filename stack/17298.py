# - 오큰수 (17298)

# input
# 4
# 3 5 2 7

# output
# 5 7 7 -1

# input
# 4
# 9 5 4 8
# -1 8 8 -1

# # 시간초과
# num = int(input())
# arr = str(input()).split(' ')
# ans = []
# for i in range(0, len(arr)):
#     target = arr[i]
#     sliced = arr[i+1::]
#     ele = '-1'
#     while sliced:
#         temp = sliced.pop()
#         if target < temp:
#             ele = temp
#     ans.append(ele)
# print(' '.join(ans))

# 
import sys
num = int(sys.stdin.readline()) 
arr = list(map(int, sys.stdin.readline().split()))
stack = []
stack.append(0)
ans = [-1] * num
for i in range(num):
    while stack and arr[i] > arr[stack[-1]]:
        ans[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)

print(' '.join(str(x) for x in ans))
