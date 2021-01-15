# N = int(input())
# lst = list(map(int, input().split(' ')))

# # 출발할 수 있는 그룹 만들기
# group=[]

# # 만들 수 있는 그룹 (1 ~ 100000)
# for i in range(1, N):
#     # 그룹 i 에 추가될 수 있는 인원 리스트
#     cur = []
#     for score in lst:
#         # 만약 공포지수가 그룹 i 보다 높거나 같다면 그룹에 추가
#         if score >= i:
#             cur.append(score)
#     # 그룹 인원이, 해당 그룹의 공포 지수 감당 인원보다 크거나 같으면 출발할 수 있는 그룹으로 분리
#     if len(cur) >= i:
#         group.append(cur)

# # 그룹 개수 출력
# print(len(group))



N = int(input())
lst = list(map(int, input().split(' ')))

lst.sort()
result = 0
count = 0
for i in }:
    count +=1 
    if i <= count:
        result += 1
        count = 0
print(result)
