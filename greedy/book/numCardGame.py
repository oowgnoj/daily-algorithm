# N * M 의 행렬이 주어지는 경우
# 마지막 카드의 수가 가장 높게 첫번째 뽑은 행을 정해야 한다. 그리고 첫번째 행에서 가장 큰 숫자를 리턴하면 된다.

[M, N]= list(map(int, input().split()))

result = 0
for i in range(M):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(min_value, result)

print(result)