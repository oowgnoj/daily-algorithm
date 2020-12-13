def solution(priorities, location):
    answer = 0
    current_location = location
    while True:
        # print("answer", answer)
        # print("max ", max(priorities))
        # print("current ", current_location)
        if priorities[0] == max(priorities):
            answer += 1
            if current_location == 0:
                break
            else:
                priorities.pop(0)
                current_location -= 1
        else:
            priorities.append(priorities.pop(0))

            if current_location == 0:
                current_location = len(priorities)-1
            else:
                current_location -= 1

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
