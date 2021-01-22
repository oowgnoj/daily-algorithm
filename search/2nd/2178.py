# (1,1) 에서 (N,M)으로 이동하는 최단거리
from collections import deque
n, m = map(int, input().split(' '))
matrix = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

# 동서남북
nx = [0,0,1,-1]
ny = [1,-1,0,0]

def bfs(i,j):
    '''0,0 부터 y,x 까지 최단 거리 리턴'''
    queue = deque([[0,0]])
    visited[0][0] = 1
    cnt = 1
    is_find = False
    while queue:
        for node in list(queue):
            y, x = node
            for i in range(4):
                my = y+ny[i]
                mx = x+nx[i]

                if my < 0 or mx < 0 or my >= n or mx >= m:
                    continue
                
                if not visited[my][mx] and matrix[my][mx]:
                    queue.append([my, mx])
                    visited[my][mx]= 1
                    if my == n-1 and mx == m-1:
                        is_find = True
                        break
        cnt +=1 
        if is_find:
            return cnt

answer = bfs(n,m)
print(answer)