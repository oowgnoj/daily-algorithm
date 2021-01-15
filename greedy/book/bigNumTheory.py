# This is Coding Test page 92

# 반복문으로 하나하나 더하는 경우
def bigNumTheory(N, M, K, arr):
  arr.sort(reverse=True)
  biggest = arr[0]
  second_biggest = arr[1]
  ans = 0
  rep = 0
  for i in range(M):
    if rep >= K:
      rep = 0
      ans += second_biggest
    else:
      ans += biggest
      rep += 1
  print(ans)

# 수학적 원리를 이용해 푸는 경우
def bigNumTheoryImp(N, M, K, arr):
    arr.sort(reverse=True)
    first = arr[0]
    second = arr[1]
    sum_of_nums = first * K + second
    num_of_repeat = M // (K+1)
    remainder = M % (K+1)
    ans = sum_of_nums * num_of_repeat + remainder * first
    print(ans)

# 수학적 원리를 이용해 푸는 경우
def bigNumTheoryFromAnswer(N, M, K, arr):
    arr.sort(reverse=True)
    first = arr[0]
    second = arr[1]
    num_of_second = M // (K+1)

    ans = 0
    ans += second * num_of_second
    ans += (M - num_of_second) * first
    print(num_of_second)
    print(ans)



[N, M, K] = list(map(int, input().split()))
arr = list(map(int, input().split()))


bigNumTheoryFromAnswer(N, M, K, arr)
