# 파라메트릭 서치
# 최대값, 최소값 혹은 값 자체를 가지고 테스트한다. 이 때 이진탐색트리의 범위는 A, B의 범위가 된다.
import sys
input = sys.stdin.readline
n, c = map(int, input().split(' '))
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()

min_val = 1
max_val = max(lst)-min(lst)

tree = [min_val, max_val]
result = 0

mid = (tree[1]+tree[0])//2
while True:
    cnt = 0
    threshold = lst[0]
    for el in lst:
        if el >= mid+threshold*cnt:
            cnt += 1
    if cnt < c:
        mid -= 1
    elif cnt > c:
        mid += 1
    else:
        break
print(cnt)
