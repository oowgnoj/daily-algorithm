# 체스판

from collections import deque

N = int(input()) # 테스트 케이스 개수
# 체스 가능한 경우의 수
nx = [1,1,2,2,-1,-1,-2,-2]
ny = [2,-2,1,-1,2,-2,-1,1]


def bfs(l, start, end):
    [start_y, start_x, ]= start
    [end_y, end_x ]= end

    # 움직인 횟수
    num_of_move = 0
    arrived = False
    
    # 보드 생성
    board = [[0 for i in range(l)] for i in range(l)] 
    # 방문 배열 생성
    visited = [[False for i in range(l)] for i in range(l)]

    queue = deque([start])
    while True:
        if arrived:
            print(num_of_move)
            break
        if not queue:
            print(0)
            break
        
        temp = deque()
        while queue:
            y,x = queue.popleft()
            visited[y][x] = True
            for i in range(8):
                cy = y+ny[i]
                cx = x+nx[i]

                if cy < 0 or cy >= l or cx < 0 or cx >= l:
                    continue
                if visited[cy][cx]:
                    continue
                if cy == end_y and cx == end_x:
                    arrived = True
                    break
                visited[cy][cx] = True
                temp.append([cy, cx])
        num_of_move += 1
        queue = temp


                

TEST_CASES = []
for i in range(N):
    # 정사각형 보드 한쪽 길이
    l = int(input())
    start = list(map(int, input().split(' ')))
    end = list(map(int, input().split(' ')))
    TEST_CASES.append((l, start, end))

for i in range(N):
    l, start, end = TEST_CASES[i]
    bfs(l, start, end)