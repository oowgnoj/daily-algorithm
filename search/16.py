from itertools import combinations
from collections import deque
import copy
N, M = map(int, input().split(' '))
board = []
for i in range(N):
    board.append(list(map(int, input().split(' '))))
zeros = []
virus = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            zeros.append((i,j))
        if board[i][j] == 2:
            virus.append((i,j))

cases = list(combinations(zeros, 3))


# 동서남북
nx = [0,0,1,-1] 
ny = [1,-1,0,0]
ans = []
for case in cases:
    case_board = copy.deepcopy(board)

    for el in case:
        case_board[el[0]][el[1]]= 1
    # 방문 확인 배열
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = deque(virus)

    while queue:
        a, b = queue.pop()
        visited[a][b] = True
        for i in range(4):
            y = a+ny[i]
            x = b+nx[i]
            if y < 0 or y >= N or x < 0 or x >= M:
                # print(x,y)
                continue
            if case_board[y][x] == 1: # 벽 
                continue
            if visited[y][x]: # 이미 방문한 경우 (최적화)
                continue

            case_board[y][x] = 2
            queue.append((y, x))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if case_board[i][j] == 0:
                cnt +=1
    ans.append(cnt)
    # case 초기화
    for el in case:
        case_board[el[0]][el[1]]= 0
print(max(ans))
