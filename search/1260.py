
# DFS 
# Depth First Search
# 시작되는 노드에서 (특정 순서대로) 연결되어있는 깊은 가지부터 탐색한다.


# BFS
# Breadth First Seach
# 시작되는 노드에서 연결되어있는 가지부터 탐색한다.
# 인접 행렬이나 인접 리스트를 만들면 계산하기 편하다.

# 1. 탐색 시작 노드를 스택에 삽입 후 방문 처리
# 2. 최상단 노드에 방문하지 않은 인접 노드가 있으면, 그 인접 노드를 스택에 넣고 방문 처리
#   - 방문하지 않은 인접 노드가 없다면, 스택에서 최상단 노드를 꺼낸다
# 2번의 과정을 더이상 수행할 수 없을 때까지 반복한다.
from collections import deque
[N, M, V]= list(map(int, input().split(' ')))

adj_matrix = [[0 for i in range(N+1)] for i in range(N+1)]
adj_matrix = [[]] + adj_matrix


for i in range(M):
    [a, b]= list(map(int, input().split(' ')))
    adj_matrix[a][b] = 1
    adj_matrix[b][a] = 1

dfs_visited = [False for i in range(N+1)]
dfs_order = []

def dfs(v):
    dfs_visited[v] = True
    dfs_order.append(v)
    for i, node in enumerate(adj_matrix[v]):
        if node == 1 and not dfs_visited[i]:
            dfs(i)

dfs(V)
print(*dfs_order)

bfs_visited = [False for i in range(N+1)]
bfs_order = []

def bfs(v):
    q = deque([v])
    bfs_visited[v] = True
    bfs_order.append(v)

    while len(q):
        v = q.popleft()
        for i, node in enumerate(adj_matrix[v]):
            if node == 1 and not bfs_visited[i]:
                bfs_visited[i] = True
                bfs_order.append(i)
                q.append(i)

bfs(V)

print(*bfs_order)

