# 이진 탐색 구현


def binary_search(arr, target, start, end):
    mid = (start+end)//2
    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return binary_search(arr, target, mid+1, end)
    else:
        return binary_search(arr, target, start, mid-1)


# # array 자체를 변형하여 자르기 보다, index로 구분하면 mid를 쉽게 구할 수 있다.
# def binary_search_book(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start+end)//2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search_book(array, target, start, mid-1)
#     else:
#       return binary_search_book(array, target, mid+1, end)


# 정렬되어있는 인덱스
lst = [1, 2, 3, 4, 5]
print(binary_search(lst, 1, 0, 4) == 0)
print(binary_search(lst, 5, 0, 4) == 4)
print(binary_search(lst, 3, 0, 4) == 2)


# lst = [1, 2, 3, 4, 5, 10, 10]
