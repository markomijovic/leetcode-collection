"""
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
"""
import numpy as np
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        if nums1 == nums2:
            return len(nums1)
        n1, n2 = len(nums1), len(nums2)
        dp = [ [0]*(n2+1) for i in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] += dp[i-1][j-1] + 1
        return np.amax(dp)