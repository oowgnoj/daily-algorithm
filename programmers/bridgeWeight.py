def solution(bridge_length, weight, truck_weights):
    timer = 0
    currentWeight = 0
    bridge = [0] * (bridge_length)
    while True:
        if not truck_weights and not bridge:
            break
        timer += 1
        bridge.pop(0)
        currentWeight = sum(bridge)
        if truck_weights:
            target = truck_weights[0]
            if currentWeight + target <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        else:
            continue
    return timer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
