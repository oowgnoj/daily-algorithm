# 반례를 찾기 힘들었음

from collections import deque
N, K = list(map(int, input().split(' ')))
visited = [False for i in range(0, 100001)]
# N이 K보다 작다면
if K < N :
    print(abs(K-N))
elif K == N:
    print(0)
else:
    q=deque([N])
    n = 0
    isFind = False
    visited[N] = True
    while q:
        temp = deque()
        while q:
            current =q.popleft()
            # +1, -1, *2
            a = current +1
            b = current -1
            c = current *2

            if a == K or b == K or c== K:
                isFind = True
                break
            if  a >= 0 and a <= 100000:
                if not visited[a]:
                    temp.append(a)
                    visited[a] = True
            if b >= 0 and b <= 100000 :
                if not visited[b]:
                    temp.append(b)
                    visited[b] = True
            if c >= 0 and c <= 100000:
                if not visited[c]:
                    temp.append(c)
                    visited[c] = True
        n+=1
        if isFind:
            break
        q = temp
    print(n)
