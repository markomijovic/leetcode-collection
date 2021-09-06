class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0: return ""
        if len(s) == 1: return s
        n = len(s)
        ans = ""
        
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]: # odd
                if (r - l + 1) > len(ans): 
                    ans = s[l:r+1]
                l -= 1
                r += 1
            
            l, r = i, i+1 
            while l >= 0 and r < n and s[l] == s[r]: # even
                if (r - l + 1) > len(ans): 
                    ans = s[l:r+1]
                l -= 1
                r += 1
                
        return ans    
        