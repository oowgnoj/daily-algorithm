# L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함

# abcd
# 3
# P x
# L
# P y

# import sys 
# string = list(sys.stdin.readline().rstrip())
# num = int(sys.stdin.readline().rstrip())
# stack=[]
# residual = []    
# for i in range(1, num +1):
#     commands = str(sys.stdin.readline().rstrip()).split(' ')
#     command = commands[0]
#     if command == 'L':
#         if stack:
#             residual.append(stack.pop())
#     if command == 'D':
#         if residual:
#             stack.append(residual.pop())
#     if command == 'B':
#         if stack:
#             stack.pop()
#     if command == 'P':
#         stack.append(commands[1])

# while (residual):
#     stack.append(residual.pop())
# print(''.join(stack))


import sys 
stack = list(sys.stdin.readline().rstrip())
num = int(sys.stdin.readline().rstrip())
residual = []    
for i in range(1, num +1):
    commands = str(sys.stdin.readline().rstrip()).split(' ')
    command = commands[0]
    if command == 'L':
        if stack:
            residual.append(stack.pop())
    if command == 'D':
        if residual:
            stack.append(residual.pop())
    if command == 'B':
        if stack:
            stack.pop()
    if command == 'P':
        stack.append(commands[1])

while (residual):
    stack.append(residual.pop())
print(''.join(stack))
