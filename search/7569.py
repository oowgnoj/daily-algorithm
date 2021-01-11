from collections import deque
R,C,H = list(map(int,input().split(' ')))
answers = []
box = []
visited = [[[False for i in range(R)] for i in range(C)] for i in range(H)]

nx = [1,-1,0,0] 
ny = [0,0,-1,1]
for h in range(H):
    floor = []
    for c in range(C):
        floor.append(list(map(int, input().split(' '))))
    box.append(floor)

def getMatures(matrix):
    matures = []
    for c in range(C):
        for r in range(R):
            if matrix[c][r]:
                matures.append([c,r])
    return matures

def dfs(h, matures: list):
    q = deque(matures)
    days = 0
    while q:
        temp = deque()
        while q:
            c, r = q.popleft()
            visited[h][c][r] = True 
            box[h][c][r] = 1

            for i in range(4):
                new_c = c + nx[i]
                new_r = r + ny[i]
                if new_c < 0 or new_c >= C or new_r < 0 or new_r >= R:
                    continue
                if visited[h][new_c][new_r]:
                    continue
                if box[h][new_c][new_r]:
                    continue

                visited[h][new_c][new_r] = True
                box[h][new_c][new_r] = 1
                temp.append([new_c, new_r])
        if temp:
            days +=1
            q = temp
    return days


for h in range(H):
    matures = getMatures(box[h])
    answers.append(dfs(h,matures))

isFalse = False
for h in range(H):
    for c in range(C):
        for r in range(R):
            if box[h][c][r] == 0:
                isFalse = True
                break
        if isFalse:
            break
    if isFalse:
        break


if isFalse:
    print(-1)
else:
    print(max(answers))
