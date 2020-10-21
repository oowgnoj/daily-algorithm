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
    lst = [[0,0]]
    # M 과 N 의 최소공배수를 구한다.
    a = 0
    b = 0
    for i in range(lcm(M,N)):
        a+=1
        b+=1
        if a % M==0:
            a = 0
        if b % N==0:
            b = 0
        lst.append([a,b])
    return lst, i


for i in range(loop):
    lst.append(list(map(int, str(input()).split(' '))))

for i in range(loop):
    print(lst)
    [M, N, x, y] = lst[i]
    lst, year = calc(M,N,x,y)
    print(year)
    



