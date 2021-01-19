# AKA LIS

# 수열 A에서 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 출력: 가장 긴 증가하는 부분의 길이를 출력
from bisect import bisect_left
n = int(input())
lst = list(map(int, input().split(' ')))
arr = [lst[0]]
for i in range(1, len(lst)):
    if lst[i] > arr[-1]:
        arr.append(lst[i])
    else:
        arr[bisect_left(arr, lst[i])] = lst[i]
print(len(arr))
