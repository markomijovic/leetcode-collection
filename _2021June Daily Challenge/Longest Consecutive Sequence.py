"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        max_seq = 0
        counter = 0
        
        for n in nums:
            
            if n-1 not in nums:
                start = n
                while start in nums:
                    start += 1
                    counter += 1
                max_seq = max(max_seq, counter)
                counter = 0
        return max_seq