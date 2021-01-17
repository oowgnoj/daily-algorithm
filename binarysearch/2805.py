import sys
input = sys.stdin.readline
n, m = map(int, input().split(' '))  # 나무의 수, 나무의 길이
lst = list(map(int, input().split(' ')))

start = 0  # 바닥에 붙여 자르는 경우
end = max(lst)  # 가장 큰 나무
result = 0
while True:
    # 탈출 문
    if start > end:
        break
    total = 0
    mid = (start+end)//2  # 중앙값으로 절단기 높이 설정
    for tree in lst:
        if tree > mid:
            total += (tree - mid)
    if total >= m:
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)
