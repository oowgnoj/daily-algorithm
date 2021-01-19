# 가장 인접한 두 공유기 사이의 거리 최대

n, k = map(int, input().split(' '))
lst = [int(input()) for _ in range(n)]
lst.sort()
# 공유기 사이의 거리
start = 1
end = max(lst)-min(lst)
ans = 1  # 초기값
while start <= end:
    mid = (start+end)//2

    # mid 값을 최대 공유기 사이의 거리라고 했을 때 -> 모든 거리가 최소 mid 는 넘어야 한다.
    value = lst[0]
    cnt = 1  # mid 로 설정했을 때 설치할 수 있는 공유기의 합
    for i in range(1, len(lst)):
        if value + mid <= lst[i]:
            value = lst[i]
            cnt += 1
    if cnt >= k:
        # 목표했던 것 보다. 더 많이 설치했다. 거리를 늘릴 수 있다.
        start = mid+1
        ans = mid
    else:
        # 목표했던 것 보다 적게 설치했다. 거리를 줄여야 한다.
        end = mid-1

print(ans)
