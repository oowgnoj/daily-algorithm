# 괄호
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(

n = int(input())

for i in range(1, n+1):
    string = str(input())
    stack = []
    ans = 'YES'
    for j in range(0, len(string)):
        if string[j] == '(':
            stack.append('x')
        if string[j] == ')':
            try:
                stack.pop()
            except:
                ans = 'NO'
    if stack:
        ans = 'NO'
    print(ans)

    