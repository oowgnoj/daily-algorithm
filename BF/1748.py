to = int(input())
# 9 : 9개
total = 0
for i in range(1,to+1):
    total += len(str(i))
print(total)
