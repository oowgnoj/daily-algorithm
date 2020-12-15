# import collections
# import copy


# def solution(prices):
#     answer = []
#     queue = collections.deque(prices)
#     while queue:
#         current_value = queue.popleft()
#         current_queue = copy.copy(queue)
#         i = 0
#         while True:
#             if not current_queue:
#                 answer.append(i)
#                 break
#             i += 1
#             compare_value = current_queue.popleft()
#             if compare_value >= current_value:
#                 continue
#             else:
#                 answer.append(i)
#                 break

#     return answer


# 효율성 - 시간초과

def solution(prices):
    answer = []
    for i, val in enumerate(prices):
        cnt = 0
        if len(prices)-1 == i:
            answer.append(cnt)
            break
        for j, compare in enumerate(prices[i+1:]):
            cnt += 1
            if compare < val or j == len(prices[i+1:])-1:
                print('here', cnt)
                answer.append(cnt)
                break

    return answer


print(solution([1, 2, 3, 2, 3]))
