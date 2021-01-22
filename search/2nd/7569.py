from collections import deque
m,n,h = map(int, input().split(' '))
matrix = []
visited=[]
for i in range(h):
    temp =[]
    visied_temp = []
    for j in range(n):
        temp.append(list(map(int, input().split(' '))))
        visied_temp.append([0 for _ in range(m)])

    matrix.append(temp)
    visited.append(visied_temp)

nx = [0,0,1,-1]
ny = [1,-1,0,0]

def bfs(array):
    queue = deque(array)
    cnt = 0
    while queue:
        temp = deque([])
        while queue:
            f,y,x = queue.popleft()
            visited[f][y][x]=1
            for i in range(4):
                mx = x + nx[i]
                my = y + ny[i]

                if mx < 0 or my < 0 or mx >= m or my >= n:
                    continue
                
                if not visited[f][my][mx] and matrix[f][my][mx] == 0 :
                    visited[f][my][mx] = 1
                    matrix[f][my][mx] = 1
                    temp.append([f,my,mx])

            if f-1 >=0 and matrix[f-1][y][x] == 0 and not visited[f-1][y][x]:
                visited[f-1][y][x] = 1
                matrix[f-1][y][x] = 1
                temp.append([f-1,y,x])

            if f+1 < h and matrix[f+1][y][x] == 0 and not visited[f+1][y][x]:
                visited[f+1][y][x] = 1
                matrix[f+1][y][x] = 1
                temp.append([f+1,y,x])
        if not temp:
            return cnt
        
        queue = temp
        cnt +=1

# print(bfs(0,1,2))

tomatoes = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1:
                tomatoes.append([i,j,k])
days = bfs(tomatoes)

is_fail = False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 0:
                is_fail = True


if is_fail:
    print(-1)
else:
    print(days)
                


