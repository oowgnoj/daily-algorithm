n = int(input())

DP = [-1] * (n+1)
# DP[1] = 1
DP[2] = True
DP[3] = True
DP[5] = True

for i in range(1, n):
    a = DP[int(i / 2)] if i % 2 ==0 else -1
    b = DP[int(i / 3)] if i % 3 ==0 else -1
    c = DP[int(i / 5)] if i % 5 ==0 else -1

    if a == True or b == True or c == True :
        print(i, a, b, c )
        DP[i] = True

    
# print(DP)
x = [i for i,el in enumerate(DP) if el == True]
x = [1] + x
print(x)
print(x[9])
print(x[3])