a = int(input())
b = a
for i in range(1, a+1):
    print(''*(b-i)+'*'*(i))
for k in range(1,b):
    print(''*(k)+'*'*(b-k))