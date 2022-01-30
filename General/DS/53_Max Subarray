class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current = nums[0]
        maxx = nums[0]

        for n in nums[1:]:
            current = max(n, current + n)
            maxx = max(maxx, current)
        return maxx
