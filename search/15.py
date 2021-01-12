from collections import deque
from sys import *
input = stdin.readline

N, M, K, X = map(int, input().split(' '))
# 도로의 개수
adj_list = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]

for i in range(M):
    a, b = list(map(int, input().split(' ')))
    adj_list[a].append(b)

queue = deque([X])
visited[X] = True
cnt = 0

# queue를 생성한다.
while queue:
    # 이번 큐에서 나오는 노드들을 한번에 관리하기 위해 temp queue를 만든다
    temp = deque()
    while queue: # queue 내부가 빌 때 까지 꺼낸다
        node=queue.popleft()
        for v in adj_list[node]:
            if visited[v]:
                continue
            # 최단거리를 구할 때는 갔던 길을 또 가지 않는다.
            visited[v]=True
            temp.append(v)
    cnt += 1
    queue = temp
    if cnt == K:
        break


if not queue:
    print(-1)
if queue:
    for i in sorted(list(queue)):
        print(i)


