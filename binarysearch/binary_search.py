# 이진 탐색 구현


# def binary_search(arr, target, start, end):
#     mid = (start+end)//2
#     if arr[mid] == target:
#         return mid
#     elif target > arr[mid]:
#         return binary_search(arr, target, mid+1, end)
#     else:
#         return binary_search(arr, target, start, mid-1)


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
# lst = [1, 2, 3, 4, 5]
# print(binary_search(lst, 1, 0, 4) == 0)
# print(binary_search(lst, 5, 0, 4) == 4)
# print(binary_search(lst, 3, 0, 4) == 2)


# lst = [1, 2, 3, 4, 5, 10, 10]


# bisect_left 구현해보기


# def bisect_left(arr, target):
#     '''정렬되어있는 array, target을 받아 이분 탐색을 사용해 
#     해당 target이 왼쪽에서 몇번 째 인덱스에 있는지 알려주는 메소드'''

#     start = 0
#     end = len(arr)-1
#     ans=None

#     while start < end:
        
#         mid = (start+end)//2  
    
#         # 왼쪽에서부터 세는 것이기 때문에 같을 때도 우선 왼쪽으로 몬다.
#         if arr[mid] >= target:
#             if arr[mid] == target:
#                 ans = mid
#             end = mid-1
#         else:
#             start = mid+1
    
#     return ans


# bisect_left() 함수가 정상 작동하는지 어떻게 증명할 수 있을까?



def bisect_left(array, target):
    start = 0
    end = len(array)-1 # -1이 필요할까?
    ans=None
    while start < end:
        mid= (start+end)//2

        # 만약 같다면 저장
        if array[mid] == target:
            ans = mid

        if array[mid] >= target: # 중앙 값을 찔렀는데, target보다 크네?
            # 작은 범위로 가자
            end = mid-1

        else:
            # 큰 범위로 가자
            start = mid+1
    return ans




def bisect_right(array, target):
    start=0
    end=len(array)
    ans=None
    while start <= end:
        mid=(start+end)//2
        print(start, end, mid)

        if array[mid] == target:
            ans = mid

        # 같은 값 처리
        if array[mid] <= target:
            start= mid+1

        else:
            end = mid-1
    return ans



print(bisect_left([1,2,2,2,2,3,4,5],2))
print(bisect_right([1,2,2,2,2,3,4,5],2))






