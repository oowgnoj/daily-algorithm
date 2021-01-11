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
    matrix.append(list(map(int, list(input()))))


# 0번째 움직임에서 벽을 부수던지, 1번째 움직임에서 벽을 부수던지, 2번째,...

# 동서남북
nx = [0,0,-1,1]
ny = [1,-1,0,0]

# 시작점
starting_point = [0,0,0]
destination_point = [C-1, R-1]
if destination_point == [0,0]:
    print(1)
else:
    q = deque([starting_point])
    move = 1
    is_arrived = False
    visited = [[[False, False] for i in range(R)] for i in range(C)]
    # [False, False] - 0번째 visited = 벽을 부수지 않은 상태. 1번째 visited = 벽을 부순 상태
    while q:
        temp = deque()
        while q: # 담겨진 queue의 요소를 다 꺼낼 때 까지
            c, r, h = q.popleft() # column, row, history(0, 1)
            visited[c][r][h] = True # 꺼낸 요소 방문처리
            
            # 꺼낸 요소에서 동, 서, 남, 북에 접근해 가능한 노드 queue에 담기
            for i in range(4):
                x = nx[i] + r # x offset
                y = ny[i] + c # y offset
                z = h # 현재 어떤 상태인지 (0: 벽을 아직 안부숨, 1: 벽을 부순 경험이 있음)

                # offset 결과 가동 범위 벗어나면 skip
                if x < 0 or x >= R or y < 0 or y >= C:
                    continue

                # 방문 했었다면 skip
                # if y == 1 and x == 4:
                #     print('######',y,x,z)
                #     print('######', visited[y][x])

                if visited[y][x][z]:
                    continue


                # 다음 행선지가 벽이라면
                if matrix[y][x] == 1:
                    # 과거 벽을 부순 경험이 있는 경우 SKIP
                    if z:
                        continue
                    # 경험 없다면 상태에 등록
                    else:
                        z=1
                
                # offset 결과 목적지에 다단 경우 break
                if destination_point == [y, x]:
                    is_arrived = True
                    break

                # 모든 예외사항 통과
                visited[y][x][z] = True # 방문 처리
                temp.append([y,x,z]) # queue에 삽입해 다음 준비

        move+=1
        if is_arrived:
            break
        else:
            q = temp



    if is_arrived:
        print(move)
    else:
        print(-1)


# 디버깅
# 반례 1)
# 5 10
# 0000011000
# 1101011010
# 0000000010
# 1111111110
# 1111000000
