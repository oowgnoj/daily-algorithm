
# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1], target = 0
# Output: 0

class Solution:
    def searchInsert(self, nums, target) -> int:
        i = 0
        if nums[-1] < target:
            return len(nums)
        while nums[i] < target: 
            i += 1
        return i

