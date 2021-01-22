from collections import deque
n = int(input())
for i in range(n):
    v, e = map(int, input().split(' '))
    adj_list = [[] for _ in range(v+1)]
    visited = [[0, None] for _ in range(v+1)]
    for j in range(e):
        a, b = tuple(map(int,input().split(' ')))
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    def bfs(n, t):
        queue = deque([[n, t]]) #vertax number, type
        visited[n][0] = 1 #visited
        visited[n][1] = t # type
        is_satisfy = True
        while queue:
            temp = deque([])
            while queue:
                flag = queue[0][1]
                n, t = queue.popleft()
                for el in adj_list[n]:
                    if visited[el][0] and flag == visited[el][1]:
                        is_satisfy = False
                        break
                    
                    elif not visited[el][0]:
                        t = 0 if flag else 1
                        temp.append([el, t])
                        visited[el][0]=1
                        visited[el][1]=t
            queue = temp
        return is_satisfy


    answer = True
    for i in range(1, v+1):
        if not visited[i][0]:
            if not bfs(i, 0):
                answer = False
    print("YES" if answer else "NO")

