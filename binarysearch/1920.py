n = int(input())
lst = list(map(int, input().split(' ')))
n_target = int(input())
targets = list(map(int, input().split(' ')))
lst.sort()


def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


for el in targets:
    print(binary_search(lst, el, 0, n-1))
