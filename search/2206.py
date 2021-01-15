# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000

# 최단경로 -> BFS
# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 
# 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 
# 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오

# 문제의 핵심
# 최단경로인데 하나의 벽을 부술 수 있다.
# 벽을 부수는 경우 
    # 1. 아예 못가서 부숨
    # 2. 조금 더 짧은 경로로 이동할 수 있기 때문에 부숨

from collections import deque
C, R = list(map(int,input().split(' ')))
matrix = []
for i in range(C):
    matrix.append(list(map(int,list(input()))))


# 0번째 움직임에서 벽을 부수던지, 1번째 움직임에서 벽을 부수던지, 2번째,...

# 동서남북
nx = [0,0,-1,1]
ny = [1,-1,0,0]

# 시작점
starting_point = [0,0]
destination_point = [C-1, R-1]
nth = 0
answers = []
while True:
    if nth >= C * R:
        break
    if starting_point == destination_point:
        answers.append(1)
        break
    q = deque([starting_point])
    move = 0
    is_arrived = False
    visited = [[False for i in range(R)] for i in range(C)]

    while q:
        temp = deque()
        while q:
            c, r = q.popleft()
            visited[c][r] = True
            for i in range(4):
                x = nx[i] + r
                y = ny[i] + c

                if x < 0 or x >= R or y < 0 or y >= C:
                    continue
                if visited[y][x]:
                    continue
                if nth != move:
                    if matrix[y][x] == 1:
                        continue
                if destination_point == [y, x]:
                    is_arrived = True
                visited[y][x] = True
                temp.append([y,x])
        q = temp
        if q or is_arrived:
            move+=1

    if is_arrived:
        nth +=1
        answers.append(move)
    else:
        nth +=1
if answers:
    print(min(answers))
else:
    print(-1)
