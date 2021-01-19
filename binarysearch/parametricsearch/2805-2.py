# 이분탐색을 선택한 이유
# 1. 제한시간 1초, N: 10억
# 2. 파라메트릭 서치
# 3. 절단기에 설정할 수 있는 높이의 최댓값

n, k = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
# 먼저 이분탐색을 위해 정렬(NlogN)
lst.sort()

# 절단기의 높이 범위
start = 0  # 양의 정수 또는 0
end = max(lst)-1  # 가장 큰 나무의 길이-1 (1<= M <= 20억)
ans = 0
while start <= end:
    mid = (start+end)//2
    cut = sum([tree-mid if tree > mid else 0 for tree in lst])

    if cut >= k:  # 더 많이 잘랐을 때
        start = mid+1
        ans = mid

    elif cut < k:  # 목표보다 더 조금 짤랐을 때
        end = mid-1
print(ans)
