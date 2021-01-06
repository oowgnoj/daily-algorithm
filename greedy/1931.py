
# 회의실의 개수는 1개
# 11 => 회의의 개수
# [시간]
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

# 조건 => 가능한 최대한 많은 회의가 개최될 수 있게.
# 정답 => print(최대한 많은 회의의 개수)

# 의문 => 그리디를 사용할 수 있을까?
# 지금 시작해서 가장 빨리 끝나는 회의를 다 더하면 괜찮아 보인다.

# N = int(input())
# meets = []
# for i in range(N):
#     meets.append(tuple(map(int,input().split(' '))))

# time = 0
# available = []
# MAX_DURATION = pow(2,31)
# MAX_TIME = 0
# for meet in meets:
#     if meet[1] > MAX_TIME:
#         MAX_TIME = meet[1]


# while True:
#     if time >= MAX_TIME:
#         break
#     candidates = [ _ for _ in meets if _[0] >= time]    
#     if not candidates:
#         break
#     target = []
#     end_time = MAX_TIME
#     for el in candidates:
#         if el[1] <= end_time:
#             target = el
#             end_time = el[1]
    
#     time = target[1]
#     available.append(target)



# print(len(available))

# 시간초과

N = int(input())
meets = []
for i in range(N):
    meets.append(tuple(map(int,input().split(' '))))

meets.sort(key=lambda x: (x[1], x[0]))

current = 0
available = []
for meet in meets:
    if current <= meet[0]:
        current = meet[1]
        available.append(meet)
print(len(available))
