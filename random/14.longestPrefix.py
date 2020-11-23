class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ''
        if strs == []:
            return ans
        target = strs[0]
    	for i in range(len(list(target))):
            for j in range(1,len(strs)):
    			if len(strs[j]) -1 < i or target[i] != strs[j][i]:
    				return ans

            ans += target[i]
        return ans





# 성능 개선
# for loop을 두번 사용하고 있음.
# O(n^2)
# 많이 포함하는 것 부터 count
# 예를 들어, ['string', 'str', 'aldjnl'] 있으면 string 부터 같나 같지 않은가 확인
# 1. 제일 짧은 string을 먼저 파악해야 함.
# 2. 제일 짧은 string 을 기준으로, 다 포함했을 때부터 한개씩 줄어드는 거
# * 시간복잡도 차이가 있을까?


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortestWord = strs[0]
        for el in strs:
        	if len(el) < len(shortestWord):
        	shortestWord = el

    	for i in range(len(shortestWord), 0, -1):
    		for el in strs:
    			if el[:i] != shortestWord[:i]:
    				return shortestWord[:i]

		return ''


        	

