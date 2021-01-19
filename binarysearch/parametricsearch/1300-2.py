# 출력: B[k]
# B = N*N의 2차원 배열(요소는 i*j)을 1차원 배열로 만들고, 정렬한 값
# [[1,2,3],[2,4,6],[3,6,9]] =>[1,2,2,3,3,4,6,6,9] #K[7] => 6

# B 배열에서 mid 이하의 수가 최소 K개는 있어야 한다.

n = int(input())
k = int(input())

start = 1
end = pow(n, 2)
ans = 0
while start <= end:
    mid = (start+end)//2

    cnt = 0
    # mid 이하의 최소 갯수
    for i in range(1, n+1):
        cnt += min(mid//i, n)

    if cnt < k:
        start = mid+1

    elif cnt >= k:
        end = mid-1
        ans = mid

print(ans)
