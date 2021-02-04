n = int(input())
lst = [list(map(int, input().split(' '))) for _ in range(n)]


for i in range(1,n):
    for j, element in enumerate(lst[i]):
        if j == 0:
            lst[i][j] = lst[i-1][j] + lst[i][j]
        elif j == len(lst[i])-1:
            lst[i][j] = lst[i-1][j-1] + lst[i][j]
        else:
            lst[i][j] = max(lst[i-1][j],lst[i-1][j-1]) + lst[i][j]
print(max(lst[n-1]))