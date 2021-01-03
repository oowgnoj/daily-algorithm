# this is coding test 118page
direction = [0, 1, 2, 3] # 북, 동, 남, 서

[N, M]= list(map(int,input().split(' ')))
[current_n, current_m, current_d] = list(map(int,input().split(' ')))

game_map = []
for i in range(N):
    # 육지 : 0, 바다 : 1
    game_map.append(list(map(int,input().split(' '))))

def changeDirection (current_direction: int):
    if current_direction == 0:
        return 3
    return current_direction -1

def goForward(current_location:list, current_direction: int):
    _current_location = current_location.copy()
    if current_direction == 0:
        _current_location[0] = _current_location[0] + 1
    if current_direction == 2:
        _current_location[0] = _current_location[0] - 1
    if current_direction == 1:
        _current_location[1] = _current_location[1] + 1
    if current_direction == 3:
        _current_location[1] = _current_location[1] -1
    return _current_location

def goBackward(current_location:list, current_direction: int):
    _current_location = current_location.copy()
    if current_direction == 0:
        _current_location[0] = _current_location[0] -1
    if current_direction == 1:
        _current_location[1] = _current_location[1]- 1
    if current_direction == 2:
        _current_location[0] = _current_location[0] +1
    if current_direction == 3:
        _current_location[1] = _current_location[1] +1
    return _current_location

current_location = [current_n, current_m]
visited = []
direction_history= []
cnt = 1

def Move():
    global current_location, current_d, visited, direction_history, cnt
    print('MOVE 함수 실행', current_location)
    current_d = changeDirection(current_d)
    next_location = goForward(current_location, current_d)
    if next_location not in visited and game_map[next_location[0]][next_location[1]] == 0:
        print('움직였음', next_location, current_d)
        cnt += 1
        direction_history= []
        visited.append(next_location)
        current_location = next_location
        Move()
    else:
        print('안움직임', current_location, current_d)
        direction_history.append(current_d)
        if len(direction_history) >= 4:
            print('동, 서 남, 북 모두 막힘')
            next_location = goBackward(current_location, current_d)
            if game_map[next_location[0]][next_location[1]] == 1:
                print('here', cnt)
                return cnt
            else:
                current_location = next_location
                direction_history = []
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
