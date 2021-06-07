class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        l = len(s)
        s1 = s[:l//2].lower()
        s2 = s[l//2:].lower()
        n1 = 0
        n2 = 0
        
        for (c1, c2) in zip(s1, s2):
            
            n1 += isVowel(c1)
            n2 += isVowel(c2)
            
        return n1 == n2
    
    
def isVowel(c) -> int:
        
    if c in ['a', 'e', 'o', 'u', 'i']:
            
        return 1
        
    else:
            
        return 0
        
    pass