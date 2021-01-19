# 배열 A: N*N 2차원 배열 (요소: i*j) [[1,2,3],[2,4,6],[3,6,9]]
# 배열 B: 배열 A를 1차원 배열로 만들어 정렬: [1,2,2,3,3,4,6,9]
# 출력: B[k]

# N은 10^5보다 작거나 같은 자연수, k는 min(10^9, N^2)
# 음. 우선 탐색해야할 공간이 너무 크다. 게다가 제한 시간이 2초다.


# 이진탐색, O(logN)
# 배열을 모두 담아 sorting 하기에는 메모리가 부족하다

# parameter : 수
n = int(input())
k = int(input())

start = 1
end = n*n
ans = 0
while start <= end:
    mid = (start+end)//2

    # 특정 수 (mid)는 B 배열에서 최소 몇번째 위치에 해당되는지(만약 여러개 있는 경우 제일 작은 index)
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n)

    if cnt >= k:
        # 밑으로
        end = mid-1
        ans = mid

    elif cnt < k:
        start = mid+1

print(ans)
