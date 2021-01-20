# https://programmers.co.kr/learn/courses/30/lessons/43236?language=python3
def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    # print(rocks)
    answer = 0
    # 거리의 최솟값을 이진 탐색
    start = 1
    end = distance

    while start <= end:
        mid = (start+end)//2
        current = 0
        cnt = 0
        for i in range(len(rocks)):
            if rocks[i] >= current + mid:
                current = rocks[i]
                continue
            else:
                cnt += 1

        # print(start, end, mid, cnt)
        # 정해놓은 최솟값이 바위를 더 많이 지워야 하면 => 거리를 줄인다.
        if cnt > n:
            end = mid - 1

        elif cnt <= n:
            start = mid + 1
            answer = mid
    return answer
