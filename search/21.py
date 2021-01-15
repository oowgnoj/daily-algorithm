from collections import deque
import math
N, MIN, MAX = map(int, input().split(' '))
matrix=[]
for i in range(N):
    matrix.append(list(map(int,input().split(' '))))

nx = [0,0,1,-1] 
ny = [1,-1,0,0]


def bfs(r, c):
    ans = []
    queue=deque([[r,c]])
    visited[r][c] = True
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            mr = r+ny[i]
            mc = c+nx[i]

            if mr < 0 or mc < 0 or mc >= N or mr >= N :
                continue
            if visited[mr][mc]:
                continue
            
            diff = abs(matrix[r][c] - matrix[mr][mc])
            if MIN <= diff <= MAX:
                visited[mr][mc] = True
                queue.append([mr,mc])
                if not ans:
                    ans.append([r,c])
                ans.append([mr,mc])
            
    return ans

days = 0
while True:
    is_find_nations = False
    visited = [[False for i in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                candidates = bfs(i,j)
                if candidates:
                    is_find_nations = True
                    total_popultation = 0 
                    for candidate in candidates:
                        total_popultation += matrix[candidate[0]][candidate[1]]
                    for candidate in candidates:
                        matrix[candidate[0]][candidate[1]] = math.trunc(total_popultation / len(candidates))
    if not is_find_nations:
        break
    else:
        days +=1

print(days)



