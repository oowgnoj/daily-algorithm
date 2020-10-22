# 예를 들어, M = 10 이고 N = 12라고 하자. 
# 첫 번째 해는 <1:1>로 표현되고, 
# 11번째 해는 <1:11>로 표현된다. 
# <3:1>은 13번째 해를 나타내고,
# <10:12>는 마지막인 60번째 해를 나타낸다. 

# 3
# 10 12 3 9
# 10 12 7 2
# 13 11 5 6

from math import gcd
def lcm(a,b):
    return a*b // gcd(a,b)

loop = int(input())
lst = []

def calc(M,N, x, y):
    e = 1
    celling = lcm(M,N)
    while M * e + x <= celling:
        x_candidate = M * e + x
        e += 1
        f = 1
        while N * f + y <= celling:
            y_candidate = N * f + y
            print(x_candidate, y_candidate)
            f = f+1
            if x_candidate == y_candidate:
                return x_candidate
    return -1



for i in range(loop):
    lst.append(list(map(int, str(input()).split(' '))))

for i in range(loop):
    [M, N, x, y] = lst[i]
    year = calc(M,N,x,y)
    print(year)
    



