class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) % 2 != 0:
            return False

        lst = list(s)
        stack = []
        while lst:
            temp = lst.pop(0)
            if temp in ['(','{','[']:
                stack.append(temp)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if curr+ temp not in ['()','{}','[]']:
                    return False
                
        if lst or stack:
            return False
        else:
            return True