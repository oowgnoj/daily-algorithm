from collections import deque
v = int(input())
n = int(input())
edges = [[0 for _ in range(v+1)] for _ in range(v+1)]
visited = [0 for _ in range(v+1)]
for i in range(n):
    a,b = map(int, input().split(' '))
    edges[a][b] = 1
    edges[b][a] = 1


# DFS / BFS 둘 중 아무거나 사용해도 큰 문제가 없다면
# BFS 를 사용하자. 구현하기에는 조금 더 시간이 걸리지만 혹시 모를 최단거리 문제 등에 대비하기 위함?
# 탐색에는 인접 리스트가 더 좋다.

def bfs(node):
    ans = 0
    queue = deque([node])
    visited[node] = 1
    while queue:
        v = queue.popleft()
        for i in range(len(edges[v])):
            if edges[v][i] and not visited[i]: # 연결되어있고, 방문하지 않았다면
                queue.append(i)
                visited[i] = 1
                ans +=1
    return ans

print(bfs(1))

