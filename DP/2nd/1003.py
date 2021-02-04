# 3
# 0
# 1
# 3



def fib(n):
    memo={}
    memo[0] = (1,0)
    memo[1] = (0,1)
    
    for i in range(n+1):
        if i not in memo:
            memo[i] = (memo[i-1][0] + memo[i-2][0], memo[i-1][1] + memo[i-2][1])
    
    return memo


n = int(input())
arr = [ int(input()) for _ in range(n) ]
memo = fib(max(arr))
for case in arr:
    print(' '.join(map(str, memo[case])))
