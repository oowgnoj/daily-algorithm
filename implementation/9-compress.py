def compress_string_nth(n, string):
    if len(string) <= 1:
        return string
    ans = ''
    temp = string[0:n]
    multiply = 0
    for i in range(0, len(string), n):
        if temp == string[i:i+n]:
            multiply +=1
        else:
            ans += str(multiply) + temp if multiply > 1 else temp
            temp = string[i:i+n]
            multiply = 1
    if multiply >= 1:
        ans += str(multiply) + temp if multiply > 1 else temp
    return ans


def solution(s):
    if len(s) <= 1:
        return len(s)
    lst = [len(compress_string_nth(nth, s)) for nth in range(1,len(s))]
    return min(lst)


