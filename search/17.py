# 경쟁적 전염
from collections import deque
C, K = map(int,input().split(' '))
matrix = [list(map(int,input().split(' '))) for i in range(C)]

visited = [[False for i in range(C)] for i in range(C)]
# S 초 후,  Y(column), X(row)
S, Y, X=map(int,input().split(' '))

def get_virus():
    answer =[]
    for i in range(C):
        for j in range(C):
            value = matrix[i][j]
            if value != 0:
                answer.append((i,j,value))
    return answer
initial_virus=get_virus()

initial_virus.sort(key=lambda x: x[2])
queue = deque(initial_virus)

ny = [0,0,-1,1]
nx = [1,-1,0,0]
time = 0

while queue:
    if time == S:
        break
    temp = deque()
    while queue:
        c, r, v = queue.popleft()
        visited[c][r]= True
        for i in range(4):
            y = c+ny[i]
            x = r+nx[i]

            if y < 0 or x < 0 or y >= C or x >= C:
                continue
            if visited[y][x]:
                continue 
            if matrix[y][x] != 0:
                continue

            visited[y][x]= True
            matrix[y][x]= v
            temp.append((y,x,v))
    time +=1
    queue = temp

print(matrix[Y-1][X-1])



