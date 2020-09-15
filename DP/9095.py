# n = 1,2,3의 합으로 나타내는 경우이ㅡ 수
# 1 = 1
# 2 = (11)(20), (02)
# 3 = (111)(210)(3) 
# 4 = 1 *4 + 

# 다이나믹 프로그래밍은 한 번 계산했던 항목을 memoization한다.
# 문제를 잘개 쪼개는데, top-down 과 bottom-up 방식이 있다.
# Topdown 방식은 재귀 형식으로 n을 구해야 했을 때 n, (n-1) , (n-2) 차례로 구한다.
# bottom - up 방식은 반복문으로 0 부터 1,2,3 .. (n-1), n차례대로 문제를 해결한다.
# 따라서 문제를 해결 가능한 형태로 쪼개는 것이 필요하다. 

# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
# 점화식: n = 1,2,3의 합으로 나타내는 경우의 수
# bottom -up 방식을 사용하면 0부터 접근해서 부분 문제를 사용해서 풀어야 한다.

# 0 -> 
# 1 -> 1
# 2 -> 1로 가능한 수 + 2로 가능한 수
# 3 -> 2로 가능한수 + 1로 가능한 수
# 4 -> n -1 ,n-2, n-3


i = int(input())
ans = []    
for i in range(i):
    num = int(input())
    memo = [-1] * (num + 1)
    if num < 3:
        ans.append(num)

    else:
        memo[0] = 1
        memo[1] = 1
        memo[2] = 2
        for j in range(3, num +1):
            memo[j] = memo[j-1] + memo[j-2] + memo[j-3]
        ans.append(memo[-1])

for el in ans:
    print(el)



