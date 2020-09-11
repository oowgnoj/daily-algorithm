# ()(((()())(())()))(())

# ans = 총 막대기 갯수
# ( -> 스택 ++
# ) -> + 갯수
# () -> + 열려있는 스택 수 

string = str(input())
opening = 0
ans = 0
isCont = False
for i in range(0, len(string)):
    if isCont:
        isCont = False
        continue
    if i < len(string) -1 and string[i] + string[i+1] == '()':
        ans += opening
        isCont = True
    elif string[i] == '(':
        opening += 1
    elif string[i] == ')' and opening:
        ans += 1
        opening -= 1
print(ans)

