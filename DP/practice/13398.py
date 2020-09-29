# n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 
# 단, 수는 한 개 이상 선택해야 한다. 또, 수열에서 수를 하나 제거할 수 있다. (제거하지 않아도 된다)
# 예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 수를 제거하지 않았을 때의 정답은 12+21인 33이 정답이 된다.
# 만약, -35를 제거한다면, 수열은 10, -4, 3, 1, 5, 6, 12, 21, -1이 되고, 여기서 정답은 10-4+3+1+5+6+12+21인 54가 된다.

# 1. requirement& analysis
# 2. design & modeling
# 3. implementation
# 4. test & release
# 5. feedback & update


n = int(input())
a = list(map(int, input().split()))
sum = [a[0]]
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
# print(sum)
# print(max(sum))


b = a.copy()
hasNegative = False
minimumNum = 0
for el in b:
    if el < 0:
        hasNegative = True
        if hasNegative and el < minimumNum:
            minimumNum = el
if hasNegative:
    del b[b.index(minimumNum)]

sumb = [b[0]]
print(b)
for i in range(1, len(b)):
    print(i, b[i])
    sumb.append(max(sum[i-1] + b[i], b[i]))
print(sumb)
print(max(sumb))