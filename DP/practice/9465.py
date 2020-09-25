# 2
# 5
# 50 10 100 20 40
# 30 50 70 10 60

# D[n] = max(D[n-1][0] + D[n][1] + D[n][2], D[n-1][1] + D[n][0] + D[n][2] , D[n-1][2] + D[n][0] + D[n][1])

import sys
num = int(input())

for num in range(num):
    n = int(sys.stdin.readline())
    a = list(map(int, str(sys.stdin.readline()).split(' ')))
    b = list(map(int, str(sys.stdin.readline()).split(' ')))
    lst = [[0,0,0]]
    DP = [[0,0,0] for _ in range(num+1)]
    for i in range(len(b)):
        lst.append([0, a[i], b[i]])
    
    for i in range(1, len(lst)):
        lst[i][0] = max(lst[i-1][0], lst[i-1][1], lst[i-1][2])
        lst[i][1] = max(lst[i-1][0], lst[i-1][2]) + lst[i][1]
        lst[i][2] = max(lst[i-1][0], lst[i-1][1]) + lst[i][2]

    print(max(lst[-1]))


