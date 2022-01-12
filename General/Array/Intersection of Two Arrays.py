"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        ans = []
        for num in nums1:
            d1[num] += 1

        for num in nums2:
            d2[num] += 1

        if len(d1) > len(d2):
            smaller = d2
            bigger = d1
        else:
            smaller = d1
            bigger = d2

        for num in smaller:
            if num in bigger:
                c = min(smaller[num], bigger[num])
                for _ in range(c):
                    ans.append(num)
        return ans
