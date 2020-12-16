class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if len(nums) < 2:
            return len(nums)
        if len(nums) == 2:
            return 1 if nums[0] == nums[1] else 2
        while True:
            if i == len(nums)-2:
                break
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
                continue
            else:
                i+=1
        return len(nums)
            
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
        return i+1
