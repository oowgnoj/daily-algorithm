import collections


# def solution(progresses, speeds):
#     deploy = collections.deque(progresses)
#     speeds = collections.deque(speeds)
#     answer = []
#     while deploy and speeds:
#         cnt = 0
#         for i in range(len(deploy)):
#             deploy[i] += speeds[i]

#         while deploy and deploy[0] >= 100:
#             cnt += 1
#             deploy.popleft()
#             speeds.popleft()

#         if cnt > 0:
#             answer.append(cnt)
#     return answer

def solution(progresses, speeds):
    deploy = collections.deque(progresses)
    speeds = collections.deque(speeds)
    answer = []
    day_count = 0
    while deploy and speeds:
        deploy_count = 0
        day_count += 1
        # print(deploy[0])
        # print(speeds[0])
        while deploy and deploy[0] + speeds[0] * day_count >= 100:
            deploy_count += 1
            deploy.popleft()
            speeds.popleft()

        if deploy_count > 0:
            answer.append(deploy_count)

    return answer


a = solution([93, 30, 55], [1, 30, 5])
print(a)
