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

# 시도
import sys
num =  int(sys.stdin.readline()) 
arr = list(map(str, sys.stdin.readline().split()))
stack = arr[::-1]
ans = ['-1'] * num
i = 0
while len(stack) > 1:
    target = stack.pop()
    temp = stack[:]
    while temp:
        val = temp.pop()
        if target < val:
            ans[i] = val
            break
    i += 1

print(' '.join(ans))



numbers = int(input())
num_list = list(map(int, input().split()))
stack = []
result = [-1 for _ in range(numbers)]

for i in range(len(num_list)):
    try:
        while num_list[stack[-1]] < num_list[i]:
            result[stack.pop()] = num_list[i]
    except:
        pass
        
    stack.append(i)
        
for i in range(numbers):
    print(result[i], end = ' ')


