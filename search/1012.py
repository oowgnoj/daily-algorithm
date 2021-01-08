T = int(input())
for i in range(T):

    [M, N, K] = list(map(int, input().split(' ')))
    grid = [[0 for i in range(M)] for i in range(N)]
    visited = [[False for i in range(M)] for i in range(N)]
    for j in range(K):
        [x, y]=list(map(int,input().split(' ')))
        grid[y][x] = 1
    cluster = []

    def bfs(x, y):
        # print("BFS 시작@@@@@@@@@@",y, x)
        if x < 0 or x >= M or y < 0 or y >= N:
            return 0
        # 방문 헀으면 빠지고
        if visited[y][x]:
            return False
        if not grid[y][x]:
            return False
        # print('방문표시', y,x)
        visited[y][x] = True

        bfs(x+1, y)
        bfs(x-1, y)
        bfs(x, y+1)
        bfs(x, y-1)
        # print(grid)
        return True
    
    cnt = 0
    for i in range(M):
        for j in range(N):
            counted = bfs(i, j)
            if counted:
                cnt +=1
    print(cnt)
            
    
    # print(cnt)

    



