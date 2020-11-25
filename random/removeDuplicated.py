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
            