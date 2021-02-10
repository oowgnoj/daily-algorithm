r, c = map(int, input().split(' '))
DP = [[-1 for _ in range(c)]for _ in range(r)]
lst = list(map(int, input().split(' ')))
matrix = []
for i in range(len(lst)):
    if i % c == 0:
        matrix.append(lst[i:i+c])

for i in range(c):    
    for j in range(r):
        if i == 0:
            DP[j][i] = matrix[j][i]
            continue
        if j == 0:
            DP[j][i] = max(DP[j][i-1], DP[j+1][i-1])  + matrix[j][i]
        elif j == r-1:
            DP[j][i] = max(DP[j][i-1], DP[j-1][i-1]) + matrix[j][i]
        else:
            DP[j][i] = max(DP[j-1][i-1], DP[j+1][i-1], DP[j][i-1])+ matrix[j][i]


print(matrix)
print(DP)