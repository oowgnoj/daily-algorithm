# 가장 긴 증가하는 부분 수열 2
from bisect import bisect_left
n = int(input())
lst = list(map(int, input().split(' ')))

arr = [lst[0]]

for i in range(1, len(lst)):
    if lst[i] > arr[-1]:
        arr.append(lst[i])
    else:
        arr[bisect_left(arr, lst[i])] = lst[i]
print(arr)
print(len(arr))
