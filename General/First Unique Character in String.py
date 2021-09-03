class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        coll = collections.Counter(s)
        
        for k, v in coll.items():
            if v == 1:
                return s.index(k)
        return - 1
        """
        unique = {}
        duplicate = {}
        for i, letter in enumerate(s):
            
            if letter in unique:
                del unique[letter]
                duplicate[letter] = 1
                continue
            elif letter not in duplicate:
                unique[letter] = i
        
        if len(unique) == 0:
            return -1
        
        return next(iter( unique.items()))[1] 
        """