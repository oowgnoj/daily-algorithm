import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split(' ')))
target_n = int(input())
targets = list(map(int, input().split(' ')))

lst.sort()


def get_target_start_index(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if (mid == 0 or array[mid-1] < array[mid]) and array[mid] == target:
        return mid
    if array[mid] >= target:
        return get_target_start_index(array, target, start, mid-1)
    else:
        return get_target_start_index(array, target, mid+1, end)


def get_target_last_index(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if (mid == end or array[mid+1] > array[mid]) and array[mid] == target:
        return mid
    if array[mid] <= target:
        return get_target_last_index(array, target, mid+1, end)
    else:
        return get_target_last_index(array, target, start, mid-1)


for el in targets:

    start = get_target_start_index(lst, el, 0, len(lst)-1)
    end = get_target_last_index(lst, el, 0, len(lst)-1)
    if start == None or end == None:
        print(0)
    else:
        print(end-start+1)
