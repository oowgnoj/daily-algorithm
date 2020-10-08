# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

num = int(input())
ans = 1
for i in range(1, num+1):
    ans *= i

count = 0
print(ans)
while ans % 10 == 0:
    ans = ans // 10 
    count +=1
print(count)

