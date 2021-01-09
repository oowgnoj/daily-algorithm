from collections import deque
[N, M] = list(map(int, input().split(' ')))
matrix = [[]]
visited = [[]]
for i in range(N):
    matrix.append([0] + list(map(int,list(input()))))

for i in range(N):
    visited.append([False for i in range(M+1)])

queue = deque([[1,1]])
visited[1][1] = True

# 동서남북
nx = [1,-1,0,0]
ny = [0,0,1,-1]
cnt = 0

while queue:
    [y, x] = queue.popleft()
    if y == N and x == M :
        print(visited[y][x])
        break

    # 동, 서, 남, 북 방향에 노드가 있는지 없는지 확인
    for i in range(4):
        ox = x+nx[i]
        oy = y+ny[i]
        if ox <= 0 or ox > M or oy <= 0 or oy > N:
            continue
        # 있다면 queue에 추가
        if matrix[oy][ox] and not visited[oy][ox]:
            queue.append([oy, ox])
            visited[oy][ox] = visited[y][x]+1
