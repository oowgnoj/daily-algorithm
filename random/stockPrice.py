import collections
import copy


def solution(prices):
    answer = []
    queue = collections.deque(prices)
    while queue:
        current_value = queue.popleft()
        current_queue = copy.copy(queue)
        i = 0
        while True:
            if not current_queue:
                answer.append(i)
                break
            i += 1
            compare_value = current_queue.popleft()
            if compare_value >= current_value:
                continue
            else:
                answer.append(i)
                break

    return answer


# 효율성 - 시간초과

print(solution([1, 2, 3, 2, 3]))
