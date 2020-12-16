class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle =='':
            return 0

        if len(needle) > len(haystack):
            return -1
            
        for i in range(len(haystack)- len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        if len(needle) > len(haystack):
            return -1
        
        for p_haystack in range(len(haystack) - len(needle) + 1):
            if self.start_comparision(haystack, needle, p_haystack, 0):
                return p_haystack
        return -1
    
    def start_comparision(self, haystack, needle, p_haystack, p_needle):
        L = len(needle)
        while p_needle < L and haystack[p_haystack] == needle[p_needle]:
            p_haystack += 1
            p_needle += 1
        return True if p_needle == len(needle) else False