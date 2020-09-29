def gcd (a,b):
    return gcd(b%a, a) if b%a else a


def getLCM(a, b):
    ''' a, c 의 최소 공배수 리턴 '''
    d = gcd(a,b)
    return d * a // d * b//d

# 최대공약수 = 
# 최소공배수 = 최대공약수 * a 를 최대공약수로 나눈 몫 * b 를 최대공약수로 나눈 몫
            
loop = int(input())
lst = []

for i in range(loop):
    [a, b]= list(map(int, str(input()).split(' ')))
    lst.append(getLCM(a,b))

for el in lst:
    print(el)



