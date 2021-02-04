n = int(input())
storages = list(map(int, input().split(' ')))

D = [0] * 100
D[0] = storages[0]
D[1] = max(storages[0], storages[1])
for i in range(2, n):
    D[i] = max(D[i-2] + storages[i], D[i-1])
print(D)
