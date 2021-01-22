# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
from collections import deque
n, m, v = list(map(int, input().split(' ')))

# 인접 행렬 vs 인접 리스트
adj_list= [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split(' '))
    adj_list[a].append(b)
    adj_list[b].append(a)


visited = [False for _ in range(n+1)]

dfs_answer = []
def dfs(adj_list, node):
    '''깊이 우선 탐색'''
    # 시작 노드 방문
    visited[node] = True
    dfs_answer.append(node)
    for el in sorted(adj_list[node]):
        if not visited[el]:
            dfs(adj_list, el)

bfs_answer = []
def bfs(adj_list, node):
    queue = deque()
    queue.append(node)
    bfs_answer.append(node)
    visited[node] = True
    while queue:
        v = queue.popleft()
        for el in sorted(adj_list[v]):
            if not visited[el]:
                queue.append(el)
                bfs_answer.append(el)
                visited[el] = True


dfs(adj_list,v)
visited = [False for _ in range(n+1)]
bfs(adj_list, v)

print(' '.join(map(str, dfs_answer)))
print(' '.join(map(str, bfs_answer)))