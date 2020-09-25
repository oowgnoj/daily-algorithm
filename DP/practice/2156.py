# 6
# 6
# 10
# 13
# 9
# 8
# 1

# D[n][j] = n개의 포도주 줄이 있을때 양의 최대, 
# 이 때 j 는 전에 어떤 포도주를 선택 했는지
# j = 0 : 전에 두개 선택
# j = 1 : n-1 과 이번거 선택


# D[n] = max(D[n-1] + D[n-2], D[n-1] +lst[n])


loop = int(input())
lst = []
DP = [[0,0] for _ in range(loop)]
# index -2, -1 배열
ans = 0
for i in range(loop):
    lst.append(int(input()))



    
print(ans)