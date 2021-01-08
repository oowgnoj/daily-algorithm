# This is Coding Test page 99

[target, dividend]=list(map(int, input().split()))
cnt = 0
while True:
    if target == 1:
        print(cnt)
        break
    cnt += 1
    if target % dividend == 0:
        target = target // dividend
    else:
        target -= 1