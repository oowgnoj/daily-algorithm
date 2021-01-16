# Binary Search
# 정렬되어있는 배열에서
# 이진 탐색으로, 갯수를 세는 문제.

n, x = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))


# def binary_search(array, target, start, end):
#     global cnt
#     if start > end:
#         return -1
#     mid = (start+end)//2

#     if array[mid] == target:
#         cnt += 1
#         binary_search(array, target, start, mid-1)
#         binary_search(array, target, mid+1, end)

#     elif array[mid] > target:
#         binary_search(array, target, start, mid-1)
#     else:
#         binary_search(array, target, mid+1, end)


# 전체의 개수를 세는 문제여서 전체를 세는 방식으로 접근했는데, 특정 요소의 첫번째, 해답에서는 마지막 인덱스를 빼는 방식으로 접근했다.
# 어떤 차이가 있을까?
# 우선 전체 개수를 세는 경우, 불필요하게 정렬되어있는 리스트의 가운데 항목까지 개수를 세게 된다.
# 한번 처음과 끝을 판별하는 이진 탐색 구조로 구현해보자.


def first(array, target, start, end):
    if start > end:
        return None

    mid = (start+end) // 2
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid

    elif array[mid] >= target:
        return first(array, target, start, mid-1)

    else:
        return first(array, target, mid+1, end)


def last(array, target, start, end):
    if start > end:
        return None

    mid = (start+end) // 2
    if (mid == end or target < array[mid+1]) and array[mid] == target:
        return mid

    elif array[mid] <= target:
        return last(array, target, mid+1, end)

    else:
        return last(array, target, start, mid-1)

    # target을 처음 찾았어도 계속 진행되어야 한다.
    # 탈출 조건은 하나의, target 요소를 발견했을 때


start = first(lst, x, 0, n-1)
end = last(lst, x, 0, n-1)

if start and end:
    print(end - start + 1)
else:
    print(-1)
