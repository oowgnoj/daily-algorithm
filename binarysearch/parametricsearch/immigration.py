# https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3
def solution(n, times):
    # 파라메트릭 서치 유형
    # n명을 모두 심사하는데 걸리는 시간 => 파라메트릭 서치
    start = 1  # 가장 적게 걸리는 시간 * 사람 수
    end = max(times) * n  # 가장 오래 걸리는 시간 * 사람 수
    ans = 0
    while start <= end:
        mid = (start+end)//2
        # 검증
        cnt = 0
        for el in times:
            cnt += mid//el

        # 값 최소
        if cnt >= n:
            end = mid-1
            ans = mid
        elif cnt < n:
            start = mid+1

    return ans
