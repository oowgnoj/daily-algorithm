from collections import deque
from sys import *
# import time
input = stdin.readline

# start_time = time.time()
N = int(input())
answers = []
def convert_edges_to_adj_list(v:int, edges: list):
    '''간선을 인접 리스트 형태로 변경'''
    lst = [[] for i in range(v+1)]
    for i in edges:
        lst[i[0]].append(i[1])
        lst[i[1]].append(i[0])
    return lst

# BFS (시작 노드, 현재 mode)
def bfs(start_node):
    if not adj_list[start_node]:
        return
    
    queue = deque([start_node])
    visited[start_node] = 1
    # 이분그래프가 맞다고 가정
    
    
    while queue:
        vertax = queue.popleft()
        for adj_v in adj_list[vertax]:
            
            # 아직 방문하지 않았으면
            if visited[adj_v] is None:
                # -1 곱하고, queue에 넣어준다
                visited[adj_v] = visited[vertax]*-1
                queue.append(adj_v)
            # 다음 값과 이전 값이 같으면 리턴한다
            elif visited[adj_v] == visited[vertax]:
                return 1
    return 0

    while queue:
        vertax = queue.popleft()
        for adj_v in adj_list[vertax]:
            # 다음값과 이전값이 같으면 리턴한다
            if visited[adj_v] == visited[vertax]:
                return 1
            # 아니면
            else:
                # 
                visited[adj_v] = visited[vertax]*-1
                queue.append(adj_v)
    return 0

for i in range(N):
    V, E = list(map(int,input().split(' ')))
    edges = []
    for i in range(E):
        edges.append(tuple(map(int,input().split(' '))))
    adj_list = convert_edges_to_adj_list(V, edges)

    # visited: 0번째 : 방문여부, 1번째: 색(0,1)
    visited = [None for i in range(V+1)]
    ans = 0

    for j in range(1, V+1):
        if visited[j] == None:
            ans = bfs(j)
            if ans == 1:
                break
    if ans == 1:
        print("NO")
    else:
        print("YES")
