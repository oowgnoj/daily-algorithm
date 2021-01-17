n, k = map(int, input().split(' '))
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()

start = 0
end = max(lst)
ans = 0
while True:
    if start > end:
        break
    mid = (start+end)//2
    if mid == 0:
        ans = 1
        break

    cnt = 0
    for el in lst:
        cnt += el // mid
    if cnt < k:
        end = mid-1
    else:
        ans = mid
        start = mid+1
print(ans)
