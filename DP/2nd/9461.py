lst = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

n = int(input())
arr = [int(input()) for _ in range(n)]

for i in range(11, max(arr)+1):
    lst.append(lst[i-1] + lst[i-5])

for el in arr:
    print(lst[el])

