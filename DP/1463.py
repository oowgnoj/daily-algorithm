# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

# 2를 계산한다고 하면, 2로 나누는게 제일 빠르다.
# 3을 계산한다고 하면 /3으로 계산하는게 제일 빠르다.
# 4를 계산한다고 하면 -1, /3 이거나, /2, /2 가 제일 빠르다.
# 5를 계산한다고 하면 -1, /2, /2 가 제일 빠르다.
# 6을 계산한다고 하면 /3, /3이다.

# 거꾸로 접근해본다고 하면




num = int(input())
array = [0 for _ in range(num+1)]

for i in range(2, num+1):
    array[i] = array[i-1] +1

    if i % 2 == 0 and array[i] > array[i//2] + 1:
        array[i] = array[i//2] + 1
    if i % 3 == 0 and array[i] > array[i//3] + 1:
        array[i] = array[i//3] + 1

print(array[num])


