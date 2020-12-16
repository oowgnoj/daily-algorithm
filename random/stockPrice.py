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
    for i in range(len(prices)):
        cnt = 0
        if len(prices)-1 == i:
            answer.append(cnt)
            break
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[j] < prices[i] or j == len(prices[i+1:])-1:
                answer.append(cnt)
                break

    return answer


print(solution([1, 2, 3, 2, 3]))
