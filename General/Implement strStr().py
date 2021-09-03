class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        """
        n = len(needle)
        fN = needle[0]
        
        for i in range(len(haystack) - n + 1):
            
            if haystack[i: i+n] == needle:
                return i
        
        return -1"""
        
        return haystack.find(needle)
    