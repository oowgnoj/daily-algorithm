# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 3가지가 있다. 
# 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 
# 단, 같은 수를 두 번 이상 연속해서 사용하면 안 된다.


# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 3가지가 있다.
# 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 
# 단, 같은 수를 두 번 이상 연속해서 사용하면 안 된다.
# D[n] =  1,2,3의 합으로 만들 수 있는 총 방법의 수 (단, 같은 수를 두 번 이상 연속해서 사용하면 안된다)
# D[n] = (D[n-1] - 끝이 1로 끝나는 것) + (D[n-2] - 끝이 2로 끝나는 것) + (D[n-3] - 끝이 3으로 끝나는 것)
# D[n] = (d[n-1][2] + d[n-1][3]) + (d[n-2][1] + d[n-2][3]) + (D[n-3][1] + d[n-3][2])


# 1 = (1)
# 2 = (2)
# 3 = (1,2), (3), (2,1)
# 4 = (3-1) + (1-1) + 1
# 5 = i = int(input())

max = int(input())
lst = [0, 1, 1, 3]
DP = [[0]*(3+1) for _ in range(100001)]
DP[1] = [0,1,0,0]
DP[2] = [0,0,1,0]
DP[3] = [0,1,1,1]

ans = []    
nums = []
maxNum = 0
for i in range(max):
    param = int(input())
    if param > maxNum:
        maxNum = param
    nums.append(param)


for j in range(4, maxNum+1):
    a = DP[j-1][2] + DP[j-1][3] % 1000000009
    b = DP[j-2][1] + DP[j-2][3] % 1000000009
    c = DP[j-3][1] + DP[j-3][2] % 1000000009
    DP[j] = [0,a,b,c]
    temp = a+b+c
    lst.append(temp)

for num in nums:
    print(lst[num] % 1000000009)




