class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """   
        d = {}
        ans = 0
        i = 0
        for j, c in enumerate(s):
            
            if c in d:
                sub_s = s[i:j]
                for k in range(len(sub_s)):
                    if sub_s[k] == c:
                        i = i+k+1
                        break
            
            d[c] = j
            ans = max(ans, j-i+1)
        return ans
        """
        d = {}
        left = 0
        ans = 0
        
        for i, c in enumerate(s):
            if c in d:
                left = max(left, d[c] + 1)
            d[c] = i
            ans = max(ans, i - left + 1)
        return ans
    