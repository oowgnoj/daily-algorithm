from collections import deque

# 최소시간 => BFS
# 회전이 들어간다.
# 동/서/남/북으로 움직일 때 회전을 상태로 포함한다. 회전이 가능하다면 회전을 한 상태로 움직이는 것도 추가한다.




nx = [0,0,1,-1]
ny = [1,1,0,0]
rotate = [0,1] # 가로, 세로

def rotate(board, y,x,f):
    if f ==0:# 가로 => 세로
        if y >= len(board)-1 or x >= len(board)-1:
            return False
        if board[y+1][x] == 1: #움직이다 걸리는 경우
            return False
        if board[y+1][x+1] ==1: #가는 그 자리가 벽인 경우
            return False
        return y,x+1,1
    else: # 세로 => 가로
        if y >= len(board)-1 or x >= len(board)-1:
            return False
        if board[y][x+1] == 1:
            return False
        if board[y+1][x+1] ==1:
            return False
        return y+1, x,0

def solution(board):
    N = len(board)
    visited = [[[0, 0] for i in range(N)] for i in range(N)]
    destination = [N-1, N-1]
    cur = [0,0,0] # y, x, form (0: 가로, 1: 세로)
    answer = 0
    queue = deque([cur])
    visited[0][0][0] = True
    while queue:
        print(queue)
        temp = deque()
        while queue:
            y,x,f=queue.popleft()
            # 동서남북으로 이동하는 경우
            for j in range(4):
                my = y+ny[j]
                mx = x+nx[j]
                
                if mx < 0 or my < 0 or mx >= N or my >= N:
                    continue
                if visited[my][mx][f]:
                    continue
                if board[my][mx] == 1:
                    continue
                visited[my][mx][f] = 1
                if [my, mx] == destination:
                    return answer
                temp.append((my,mx,f))

            
            # 회전하는 경우
            rotated = rotate(board,y,x,f)
            if not rotated:
                continue
            else:
                y,x,f=rotated
                visited[y][x][f] = 1
                if [y, x] == destination:
                    return answer
                temp.append(rotated)
        queue = temp
        answer +=1

                
                

    print(answer)
    return answer

print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]) == 7)