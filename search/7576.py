from collections import deque
[C, R]= list(map(int,input().split(' ')))
tomatoes = []
for i in range(R):
    tomatoes.append(list(map(int,input().split(' '))))

visited = [[False for i in range(C)] for i in range(R)]
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 없음
answer = []

candidates = []

for r in range(R):
    for c in range(C):
        if tomatoes[r][c] == 1:
            candidates.append([r,c])


# 동서남북
nx = [1,-1,0,0] 
ny = [0,0,-1,1]

def bfs(list):
    '''c,r 에서 시작해서 주변에 더이상 익을 토마토가 없을 때까지 작동, 그리고 총 일수를 리턴'''
    days = 0
    queue=deque(list)
    while True:
        if not queue:
            break
        temp = deque()
        while queue:
            # queue의 모든 노드 빼기
            r, c = queue.popleft()
            
            # 동서남북에 있는 노드 더하기
            for i in range(4):
                nc = c + nx[i]
                nr = r + ny[i]
                if nc < 0 or nc >= C or nr < 0 or nr >= R:
                    continue

                if tomatoes[nr][nc] == 0 and not visited[nr][nc] == 1 and tomatoes[nr][nc] != -1 :
                    temp.append((nr,nc))
                    visited[nr][nc] = True
                    tomatoes[nr][nc] = 1

        queue = temp
        if queue:
            days += 1
    return days


days = bfs(candidates)


hasFalse = False
for r in range(R):
    for c in range(C):
        if tomatoes[r][c] == 0:
            hasFalse = True
            break
        
if hasFalse:
    print(-1)
else:
    print(days)

