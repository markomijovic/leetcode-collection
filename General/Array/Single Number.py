"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1

        for k, v in d.items():
            if v == 1:
                return k
        return -1

    # or just xor bit operation for num in nums: ans = ans ^ num (^ is the xor operator)
