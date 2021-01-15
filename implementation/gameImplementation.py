# this is coding test 118page
[N, M]= list(map(int,input().split(' ')))
visited = [[0]* N for _ in range(M)]
[current_x, current_y, current_d] = list(map(int,input().split(' ')))

game_map = []
for i in range(N):
    # 육지 : 0, 바다 : 1
    game_map.append(list(map(int,input().split(' '))))



direction = [0, 1, 2, 3] # 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def changeDirection():
    global current_d
    if current_d == 0:
        current_d = 3
    else:
        current_d = current_d -1

turn_time= 0
cnt = 1
visited[current_x][current_y] = 1

def Move():
    global current_x, current_y, current_d, visited, turn_time, cnt
    changeDirection()
    next_x = current_x + dx[current_d]
    next_y = current_y + dy[current_d]
    if visited[next_x][next_y] == 0 and game_map[next_x][next_y] == 0:
        cnt += 1
        current_x = next_x
        current_y = next_y
        turn_time= 0
        visited[current_x][current_y] = 1
        Move()
    else:
        turn_time += 1
        if turn_time == 4:
            next_x = current_x - dx[current_d]
            next_y = current_y - dy[current_d]
            if game_map[next_x][next_y] == 1:
                # 바다인 경우
                print('here', cnt)
                return cnt
            else:
                current_x = next_x
                current_y = next_y
                turn_time = 0
        Move()

Move()
    



# 이동 규칙 
# 1. 현재 위치, 현재 방향에서 changeDirection
# 2. if changeDirection() 했는데, 가보지 않은 칸이 있다면:
#       changeDirection()
#       goFoward()
#    else:
#       changeDirection()
#       1단계로 돌아가기
# 3. if 네 방향 모두 가본 칸이나, 바다:
#       if goBackward():
#           goBackward():
#           1단계
#       else:
#           끝
# 


# 삭제
# def goForward(current_location:list, current_direction: int):
#     _current_location = current_location.copy()
#     if current_direction == 0:
#         _current_location[0] = _current_location[0] + 1
#     if current_direction == 2:
#         _current_location[0] = _current_location[0] - 1
#     if current_direction == 1:
#         _current_location[1] = _current_location[1] + 1
#     if current_direction == 3:
#         _current_location[1] = _current_location[1] -1
#     return _current_location

# def goBackward(current_location:list, current_direction: int):
#     _current_location = current_location.copy()
#     if current_direction == 0:
#         _current_location[0] = _current_location[0] -1
#     if current_direction == 1:
#         _current_location[1] = _current_location[1]- 1
#     if current_direction == 2:
#         _current_location[0] = _current_location[0] +1
#     if current_direction == 3:
#         _current_location[1] = _current_location[1] +1
#     return _current_location

