"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        nums.sort() # O(nlogn)
        if n <= 3:
            return sum(nums)
        ans = sys.maxsize
        
        for i in range(n - 2):
            first = nums[i]
            j = i+1
            k = n-1
            while (j < k):
                sumarr = first + nums[j] + nums[k]
                if sumarr == target:
                    return sumarr
                elif sumarr > target: # means we're over, so decrease the max
                    k -= 1
                else: # we're under so increase min
                    j += 1
                # last update the answer if the sum is closer to the target
                if abs(sumarr - target) < abs(ans - target):
                    ans = sumarr
        return ans