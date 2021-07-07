"""
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.
"""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        freq = {}
        l = len(arr) / 2
        
        for val in arr: # O(N)
            if val in freq:
                freq[val] += 1
            else:
                freq[val] = 1
        
        highest_freq = list(reversed({k: v for k, v in sorted(freq.items(), key=lambda item: item[1])}))
        sum = 0
        ans = 0
        for key in highest_freq:
            sum += freq[key]
            ans += 1
            if sum >= l:
                break
        return ans