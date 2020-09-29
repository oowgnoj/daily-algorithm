# 8

# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1

num = int(input())
series = []
for i in range(1, num+1):
    series.append(int(input()))

stack = []
increase = 1
pointer = 0
msg = ''
no = False
while(pointer < num):
    if stack != [] and stack[-1] == series[pointer]:
        pointer = pointer + 1
        stack.pop()
        msg = msg + '-\n'
    elif increase <= num:
        stack.append(increase)
        increase = increase + 1
        msg = msg + '+\n'
    else:
        no = True
        break
if no:
    print("NO")
else:
    print(msg[0:-1])