string = str(input())
# 0이 나오는 경우
    # 첫번째에 0이 나오면
        # string[0] + string[1]
    # 중간에 0이 나오면
        # if 여태까지 결과가 0이면
            # total + string[i]
        # else:
            # total * string[i]

total = 0
for target in string:
    target = int(target)
    if total * target == 0:
        # 곱한 값이 0이면 더하고
        total += target
    else:
        # 아니면 곱한다.
        total *= target

print(total)


# x * 1 < x + 2 when x == 1
