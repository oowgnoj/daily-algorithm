n = int(input())
steps =[int(input()) for _ in range(n)]
DP=[0]
DP.append(steps[0])
DP.append(steps[0]+steps[1])


for i in range(2, n):
    steps[i] + steps[]
print(DP)
