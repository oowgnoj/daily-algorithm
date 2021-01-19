# 왜 이분 탐색으로 풀어야 하는가
# 1<=N<=100,000 / 1<=M<=100,000 의 조건에서 N*M을 수행하면
# 최대의 경우10,000,000,000 100억의 연산횟수를 초과한다.
# 파이썬의 경우 최대 초당 최대 10억 까지 연산이 가능하므로 시간초과를 받을 가능성이 농후하기 때문에

# import sys
# input = sys.stdin.readline
# n = int(input())
# n_lst = list(map(int, input().split(' ')))
# t = int(input())
# t_lst = list(map(int, input().split(' ')))

# n_lst.sort()  # 넘버 리스트 정렬

# for target in t_lst:
#     start = 0
#     end = len(n_lst)-1
#     is_exist = False
#     while start <= end:
#         mid = (start+end)//2
#         if n_lst[mid] == target:
#             is_exist = True
#             break
#         elif n_lst[mid] < target:
#             start = mid+1
#         else:
#             end = mid-1

#     print(1) if is_exist else print(0)


import sys
input = sys.stdin.readline
input()
number_set = set(input().strip().split(' '))
input()
t_lst = list(input().strip().split(' '))
for el in t_lst:
    print(1) if el in number_set else print(0)
