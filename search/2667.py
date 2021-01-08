n = int(input())
grid= []
visited= [[False for _ in range(n)] for i in range(n)]
cluster = []
for i in range(n):
    grid.append(list(map(int, input())))

def dfs(x, y):
    cnt = 0
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if not grid[x][y]:
        return False
    if visited[x][y]:
        return False
    visited[x][y] = True
    return 1 + dfs(x,y+1) + dfs(x,y-1) + dfs(x+1,y) + dfs(x-1,y)

for i in range(n):
    for j in range(n):
        cnt = dfs(i,j)
        if cnt:
            cluster.append(cnt)

print(len(cluster))
cluster.sort()
for num in cluster:
    print(num)