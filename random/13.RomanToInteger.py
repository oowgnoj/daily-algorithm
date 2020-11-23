class Solution(object):
    roman = {"I":1, "V":5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

    	lst = list(lst)
    	answer = 0
    	for i, num in enumerate(lst, start=0):
    		if roman[lst[i]] < roman[lst[i+1]]:
    			answer -= roman[lst[i]]
    			continue
    		answer += roman[lst[i]]

		return answer

