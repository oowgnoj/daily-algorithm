# 2206
# (1,1) 에서 (n,m) 까지 가는데 최단거리 (단 벽을 하나까지 부실 수 있다.)


# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000

from collections import deque
n, m = map(int, input().split(' '))
matrix = [list(map(int,input())) for _ in range(n)]
visited = [[[0,0] for _ in range(m)] for _ in range(n)] # [방문 stamp, 상태 (0: 벽 부순 경험 없음, 1: 벽 부순 경험 있음)]

nx = [0,0,1,-1]
ny = [1,-1, 0, 0]



def bfs(y,x,state):
    queue = deque([[y,x,state]])
    visited[y][x][state] = 1
    cnt = 1
    is_find = False
    while queue:
        temp = deque([])
        while queue:
            y, x, has_history = queue.popleft()
            for i in range(4):
                mx = x + nx[i]
                my = y + ny[i]

                if mx < 0 or my < 0 or mx >= m or my >= n:
                    continue
                
                if visited[my][mx][has_history]:
                    continue

                if mx == m-1 and my == n-1:
                    is_find = True
                    break

                if matrix[my][mx] == 1 and not has_history: # 벽을 부수는 경우
                    temp.append([my,mx,1])
                    visited[my][mx][1] = 1

                elif matrix[my][mx] == 0: # 원래 지나갈 수 있는 경우
                    temp.append([my,mx,has_history])
                    visited[my][mx][has_history] = 1
        
        queue = temp
        cnt +=1
        if is_find:
            return cnt
    return -1

if n == 1 and m == 1:
    print(1)
else:
    print(bfs(0,0,0))

    


                    