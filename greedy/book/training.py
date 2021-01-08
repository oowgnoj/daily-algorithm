def solution(n, lost, reserve):
    answer = 0
    for i, res_s in enumerate(reserve):
        print(i,'번째')
        for j, lost_s in enumerate(lost):
            if abs(res_s - lost_s) == 1:
                print(reserve[i], lost[j])
                del reserve[i]
                del lost[j]
                print(reserve, lost)
                break
            if abs(res_s - lost_s) == 0:
                del reserve[i]
                del lost[j]
                print('here')
                break
        print(reserve)
    return n - len(lost)