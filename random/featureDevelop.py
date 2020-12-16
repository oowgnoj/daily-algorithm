import collections


def solution(progresses, speeds):
    deploy = collections.deque(progresses)
    speeds = collections.deque(speeds)
    answer = []
    while deploy and speeds:
        cnt = 0
        for i in range(len(deploy)):
            deploy[i] += speeds[i]

        # print(deploy)
        while deploy and deploy[0] >= 100:
            cnt += 1
            deploy.popleft()
            speeds.popleft()

        print(cnt)
        answer.append(cnt)
    return answer


solution([93, 30, 55], [1, 30, 5])
