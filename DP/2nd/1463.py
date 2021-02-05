x = int(input())
DP = [[x]]

def get_cnt(n):
    temp = []
    if n % 3 == 0:
        temp.append(n//3)
    if n % 2 == 0:
        temp.append(n//2)
    temp.append(n-1)
    return temp


while 1 not in DP[-1]:
    temp = []
    for el in DP[-1]:
        temp+= get_cnt(el)
    DP.append(temp)

print(DP)
print(len(DP)-1