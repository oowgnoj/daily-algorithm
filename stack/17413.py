# - 단어뒤집기 2 (17413)
# 공백으로 나누어져있는 단어를 뒤집는다.
# < > 태그 내부에 있는 문자열은 뒤집지 않는다.

# split 하는 것이 까다로울 수 있다. 
# 문자열을 forloop 하다가 '<' 부터 '>'는 그냥 ans에 추가하고, 단어가 나오면 stack에 추가해 공백이 생길 때 까지 (끝날 때 까지) 넣고, 뺀다
# a = int(input())
# for i in range(1, a+1):
#   string = str(input())
#   reverse = ''
#   stack =[]
#   for j in range(0, len(string)):
#     if string[j] == ' ':
#       while(stack):
#         alphabet = stack.pop()
#         reverse = reverse + alphabet
#       reverse = reverse + ' '
#       stack = []
#     else:
#       stack.append(string[j])
#   if stack:
#      while(stack):
#         alphabet = stack.pop()
#         reverse = reverse + alphabet
#   print(reverse)




string = str(input())
stack =[]
isTag = False
ans = ''
for i in range(0, len(string)):
    if string[i] == '<':
        while stack:
            ans = ans + stack.pop()
        isTag = True
    if isTag:
        ans = ans + string[i]
    if string[i] == '>':
        isTag = False
        continue
    
    if not isTag and string[i] == ' ':
        while(stack):
            ans = ans + stack.pop()
        ans = ans + ' '
        stack = []
    elif not isTag:
        stack.append(string[i])    

while(stack):
    ans = ans + stack.pop()

print(ans)