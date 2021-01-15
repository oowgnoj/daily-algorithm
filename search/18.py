def is_good_string(string):
    answer = True
    open_p = 0
    front = '('
    back = ')'
    for i in string:
        if i == front:
            open_p +=1
        elif i == back:
            open_p -=1
        if open_p <0:
            answer = False
            break
    return answer

def split_string(p):
    front = '('
    back = ')'
    open_p = 0
    for i, string in enumerate(p):
        if string == front:
            open_p +=1
        elif string==back:
            open_p -=1
        
        if open_p == 0:
            return p[:i+1], p[i+1:] 

def reverse(p):
    answer = ''
    for i in p:
        if i == '(':
            answer += ')'
        else:
            answer += '('
    return answer
def solution(p):
    if p == '':
        return ''
    if is_good_string(p):
        return p
    
    # 2번
    u, v = split_string(p)
    if is_good_string(u):
        return u + solution(v)
    else:
        string = '('
        string += solution(v)
        string += ')'
        u = reverse(u[1:-1])

        string= string+ u
        return string
