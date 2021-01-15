# (a, b) 순서 쌍으로 간선이 주어질 때
from collections import deque

n = int(input())
edges_n = int(input())

edges =  [[] for i in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for i in range(edges_n):
    [a, b]=list(map(int, input().split(' ')))
    edges[a].append(b)
    edges[b].append(a)

# def dfs(v):
#     visited[v] = True
#     for node in edges[v]:
#         if not visited[node]:
#             dfs(node)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while len(queue):
        node = queue.popleft()
        for n in edges[node]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)

    

bfs(1)
print(visited.count(True) -1)


