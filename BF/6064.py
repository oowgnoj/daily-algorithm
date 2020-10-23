# 예를 들어, M = 10 이고 N = 12라고 하자. 
# 첫 번째 해는 <1:1>로 표현되고, 
# 11번째 해는 <1:11>로 표현된다. 
# <3:1>은 13번째 해를 나타내고,
# <10:12>는 마지막인 60번째 해를 나타낸다. 

# 3
# 10 12 3 9
# 10 12 7 2
# 13 11 5 6



def calc(M,N, x, y):
    while x <= M*N:
        if (x-y)%n ==0:
            return x
        x=x+M
    return -1



t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(calc(m, n, x, y))




