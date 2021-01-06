# N 개의 동전 갯수로 K의 가치를 만들어 내기

[N, K] = list(map(int, input().split(' ')))
values = []
for i in range(N):
    value = int(input())
    values.append(value)

answer = 0
values.sort(reverse=True)
for value in values:
    if K < value or K == 0:
        continue

    num_coin = K // value
    answer += num_coin
    K = K - num_coin * value

print(answer)

