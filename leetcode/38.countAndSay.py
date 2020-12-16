# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"


class Solution:
    def _say(self, string):
        if len(string) == 1:
            return string
        
        target = string[0]
        cnt = 1
        ans = ''
        for i in range(1,len(string)):
            if target != string[i]:
                ans = ans + cnt + target
                cnt = 0
                target=string[i]
            else:
                cnt += 1
        return ans
                

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        self.countAndSay(n-1)


# countAndSay(4)

def _say(string):
    if len(string) == 1:
        return string
    
    target = string[0]
    cnt = 1
    ans = ''
    for i in range(1,len(string)):
        if target != string[i]:
            ans = ans + cnt + target
            cnt = 0
            target=string[i]
        else:
            cnt += 1
    return ans

# test case
print('########## test case start ###########')
result_11 = _say('11')
print('## 11 should be 21', result_11 == '21')
if result_11 != '21':
    print("##### wrong case for 11")
    print(_say('11'))