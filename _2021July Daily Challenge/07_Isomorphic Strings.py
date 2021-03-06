"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""
class Solution:
    # O(n)
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        # idea: map each character from s to the corresponding character in t
        # keep track of the mapping in a dict
        d = {}
        for i, letter in enumerate(s):
            if letter not in d:
                if t[i] not in d.values():
                    d[letter] = t[i]
                else:
                    return False
            else:
                if t[i] != d[letter]:
                    return False
        return True