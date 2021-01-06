def countFromA(alphabet):
    if alphabet == 'A':
        return 0
    o = ord(alphabet) - ord('A') 
    i = ord('Z') - ord(alphabet) + 1
    return min(o, i)
    
def solution(name):
    cnt = 0
    _name = list(name)
    ox = [True if _ == 'A' else _ for _ in _name]
    i = 0
    while True:
        cnt += countFromA(_name[i])
        print(_name[i], '!!!!!!!', countFromA(_name[i]))
        ox[i] = True
        if ox.count(True) == len(_name):
            break

        for j in range(1, len(_name)):
            if _name[i+j] != True:
                i = i + j
                cnt += i
                break
            if _name[i-j] != True:
                i = i - j
                cnt += i
                break
    print(cnt)
                
            
        
            
solution("JAN")
solution("JEROEN")