# 본격적으로 상/하/좌/우에 해당하는 문제가 나왔다.
# 약간의 난이도를 주려면 이런 방식을 많이 사용하는 것 같다.
# 먼저 BFS/DFS 중 어떤 것을 사용하는게 좋을지 판단할 수 있는데 가급적이면 BFS를 사용하자


from collections import deque
n = int(input())
matrix = [list(map(int,input())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
# 이 문제같은 경우에, (0,0) 부터 (n,n) 까지 반복문으로 돌아가면서 만약
#  집이 있는데 방문하지 않았다면 BFS를 돌려주고, 단지수를 하나 늘리면 된다

ny = [0,0, 1,-1]
nx = [1,-1,0,0]

def bfs(i,j):
    cnt = 1
    queue = deque([[i,j]])
    visited[i][j] = 1
    while queue:
        y,x = queue.popleft()
        for i in range(4): # 동 서 남 북
            my = y + ny[i]
            mx = x + nx[i]

            if my < 0 or mx < 0 or mx >= n or my >= n:
                continue

            if matrix[my][mx] and not visited[my][mx]:
                queue.append([my,mx])
                visited[my][mx] = 1
                cnt +=1
    return cnt


ans = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and matrix[i][j]:
            ans.append(bfs(i,j))

print(len(ans))
for el in sorted(ans):
    print(el)