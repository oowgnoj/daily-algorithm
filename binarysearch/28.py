n = int(input())
lst = list(map(int, input().split(' ')))
lst.sort()


# 고정점 찾기 (i == lst[i])
# binary search 활용해서 찾기
# 없다면 -1 리턴


def binary_search(n, lst, start, end):
    # 시작하는 index 보다 끝나는 index가 크면(즉 재귀가 길이보다 많이 실행되면 리턴)
    if start > end:
        return -1

    mid = (start+end)//2  # 중앙값 -> 길이/2 의 몫 (버림)

    # index와 값이 같다면
    if mid == lst[mid]:
        # index  리턴
        return mid

    # 값이 index 보다 클 때

    elif lst[mid] > mid:
        # mid 기준으로 왼쪽 부분 탐색
        return binary_search(n, lst, start, mid-1)
    else:
        # mid 기준으로 오른쪽 부분 탐색
        return binary_search(n, lst, mid+1, end)
