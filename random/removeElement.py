class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) < 1:
            return len(nums)
        i = 0
        j = 0
        while True:
            if nums[i] == val and nums[j] == val:
                j+=1
            elif nums[i] == val and nums[j] != val:
                temp = nums[i]
                nums[i]= nums[j]
                nums[j] = temp
                i+=1
                j+=1
            elif nums[i] != val and nums[j] == val:
                i+=1
                j+=1
            elif nums[i] != val and nums[j] != val:
                i+=1
                j+=1
            if j == len(nums):
                return i


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
                
            
        return i