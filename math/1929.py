import math
def isPrime(num):
    isTrue = True
    if num == 1:
        return False
    
    to = int(math.sqrt(num))
    for j in range(2, to+1):
        if num % j == 0 :
            isTrue = False
            break

    return isTrue

lst = list(map(int, str(input()).split(' ')))
for i in range(lst[0], lst[1]+1):
    if isPrime(i):
        print(i)
