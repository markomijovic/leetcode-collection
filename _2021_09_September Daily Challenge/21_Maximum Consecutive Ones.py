"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # window starts when a 1 follows a 0  110|1
        # window ends when a 0 follows a 1  11|01
        ans = 0
        
        left = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                ans = max(ans, left)
                left = 0
            else:
                left += 1
        return max(ans, left)
                