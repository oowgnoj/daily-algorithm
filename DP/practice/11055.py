# 문제
# 수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

# 원소가 n개인 배열의 일부 원소를 골라내서 만든 부분 수열 중, 
# 각 원소가 이전 원소보다 크다는 조건을 만족하고, 그 길이가 최대인 부분 수열을 최장 증가 부분 수열이라고 합니다.
# 예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 
# 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 합이 가장 큰 증가 부분 수열의 합을 출력한다.

# 예제 입력 1 


# 10
# 1 100 2 50 60 3 5 6 7 8
# 예제 출력 1 
# 113



num = int(input())
lst = list(map(int, str(input()).split(' ')))

DP = [0 for _ in range(num)]
for i in range(num):
    DP[i] = lst[i]
    for j in range(i):
        if lst[i] > lst[j] and DP[i] < DP[j]+ lst[i]:
            DP[i] = DP[j] + lst[i]

print(max(DP))