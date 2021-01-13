# 선생님 경로가 닿고, 학생이 있는 경로를 다 수집하고
# 조합으로 경우의 수를 구해서
# 3개 뽑아서 만약 다 가려지면, clear

# 근데 S랑 T랑 붙어있으면 무조건 안됨
from collections import deque
from itertools import combinations
N = int(input())
board = []

visited = [[False for i in range(N)] for i in range(N)]

for i in range(N):
    board.append(list(map(str, input().split(' '))))

teachers = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            teachers.append((i,j))


def get_candidates(r,c, nx, ny):
    # 동, 서, 남, 북으로 끝까지 (선생님, 학생, 벽이 있을 때 까지) 간다
    # 만약 동,서,남,북 방향으로 움직이다가 그 방향에서 학생을 만나면 움직인 모든 경로를 리턴한다
    r = r+ny
    c = c+nx
    visited = [[False for i in range(N)] for i in range(N)]

    if r < 0 or c < 0 or r >= N or c >= N:
        return
    if board[r][c] == "S":
        return
    if board[r][c] == "T":
        return
    if not visited[r][c]:
        candidates.append([r,c])
    get_candidates(r,c,nx,ny)

nx = [0,0,1,-1]
ny = [1,-1,0,0]

candidates = []
for el in teachers:
    for d in range(4):
        x, y = el
        get_candidates(x,y,nx[d],ny[d])

def bfs(r, c, nx, ny):
    my = r+ny
    mx = c+nx
    if my < 0 or mx < 0 or my >= N or mx >= N:
        return False
    elif board[my][mx] == 'O':
        return False
    elif board[my][mx] == 'T':
        return False
    elif board[my][mx] == 'S':
        return True
    elif board[my][mx] == 'X':
        return bfs(my,mx,nx,ny)


cases=list(combinations(candidates, 3))


for case in cases:
    is_arrest = False
    # case 적용
    for i in range(3):
        board[case[i][0]][case[i][1]] = 'O'
    # board 검증
    for teacher in teachers:
        r,c = teacher
        for d in range(4):
            _is_arrest = bfs(r,c, ny[d],nx[d])
            if _is_arrest:
                is_arrest = True
                break
    if not is_arrest:
        break
    # case 초기화
    for i in range(3):
        board[case[i][0]][case[i][1]] = 'X'

if not is_arrest:
    print('YES')
else:
    print('NO')