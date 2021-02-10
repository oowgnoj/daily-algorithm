n = int(input())
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
k = int(input())
for i in range(k):
    x, y = list(map(int,input().split(' ')))
    matrix[x][y] = 1

l = int(input())
rotates = [input().split(' ') for _ in range(l)]


current = [[1, 1], [1, 1]] # 머리, 꼬리
index = 0
seconds = 0
direction = 1 # 0: 상, 1: 우, 2: 하, 3: 좌


def rotate():
    global index, direction
    if rotates[index][1] == 'L':
        direction = direction -1 if direction != 0 else 3
    else:
        direction = direction +1 if direction != 3 else 0
    print("ROTATE", direction)

def default_move():
    global direction, current
    if direction == 0:
        current[0][0] -= 1
    elif direction == 1:
        current[0][1] += 1
    elif direction == 2:
        current[0][0] += 1
    elif direction == 3:
        current[0][1] -= 1
        
while True:
    seconds +=1
    if index < len(rotates) and seconds == int(rotates[index][0]):
        rotate()
        index += 1

    default_move()

    x, y = current[0]

    if x > n or y > n or x < 1 or y < 1:
        break

    if matrix[current[0][0]][current[0][1]] == 1:
        matrix[current[0][0]][current[0][1]] = 0
        print('eat apple')

    else:
        if direction == 0:
            current[1][0] -= 1
        elif direction == 1:
            current[1][1] += 1
        elif direction == 2:
            current[1][0] += 1
        elif direction == 3:
            current[1][1] -= 1
    print(seconds, '==>', current)
print(seconds)
