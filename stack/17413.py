# - 단어뒤집기 2 (17413)
# 공백으로 나누어져있는 단어를 뒤집는다.
# < > 태그 내부에 있는 문자열은 뒤집지 않는다.


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