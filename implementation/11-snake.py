n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
k = int(input())
for i in range(k):
    x, y = list(map(int,input().split(' ')))
    matrix[x][y] = 1

l = int(input())
rotates = [input().split(' ') for _ in range(l)]

current = [[0, 0], [0, 0]] # 머리, 꼬리
index = 0
seconds = 0
direction = 1 # 0: 상, 1: 우, 2: 하, 3: 좌

while True:

    # 변경
    if index < len(rotates) and  seconds == int(rotates[index][0]):
        if rotates[index][1] == 'C':
            direction = direction -1 if direction != 0 else 3
        else:
            direction = direction +1 if direction != 3 else 0
        index += 1
        print(rotates[index])
        continue

    #기본 동작
    else:
        if direction == 0:
            current[0][0] -= 1
        elif direction == 1:
            current[0][1] += 1
        elif direction == 2:
            current[0][0] += 1
        elif direction == 3:
            current[0][1] -= 1
        
    # 벽 부딪히면 break
    x, y = current[0]
    if x >= n or y >= n:
        break

    # 사과 ?
    # print(current[0][0],current[0][1])
    # print(matrix)
    if matrix[current[0][0]][current[0][1]] == 1:
        matrix[current[0][0]][current[0][1]] = 0

    else:
        if direction == 0:
            current[1][0] -= 1
        elif direction == 1:
            current[1][1] += 1
        elif direction == 2:
            current[1][0] += 1
        elif direction == 3:
            current[1][1] -= 1

    print(current)
    seconds +=1
# print(matrix)

print(seconds)
