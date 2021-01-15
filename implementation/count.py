# this is coding test page 113

def countIf3(N):
    H = N
    M = 60
    S = 60
    cnt = 0
    for h in range(H+1):
        for m in range(M):
            for s in range(S):
                if '3' in str(h) + str(m) + str(s):
                    cnt += 1
    print(cnt)
    
countIf3(5)