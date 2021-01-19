# N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다.

# 문제에서 최대 랜선의 길이를 구하라고 했다.
# 미지수 : 최대 랜선의 길이

k, n = map(int, input().split(" "))  # 이미 가지고 있는 개수, 필요한 개수
lst = []
for i in range(k):
    lst.append(int(input()))

# 이분 탐색의 주체로 랜선의 길이가 되어야 하는데 이 때
start = 1  # 최소 값
end = sum(lst)//n  # 최대 값
ans = 0

# 왜냐하면 0 이하의 길이로는 자를 수 없고, 최대값을 초과하여 자른다면 지금 있는 그대로이기 때문에
while start <= end:
    # 최대값, 최소값으로 만든 랜선의 길이
    mid = (start+end)//2
    cnt = sum([line//mid for line in lst])
    if cnt >= n:
        start = mid+1
        ans = mid
    else:
        end = mid-1
print(ans)
