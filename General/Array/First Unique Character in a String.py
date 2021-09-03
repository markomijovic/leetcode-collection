"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:

        unique_dict = {}
        duplicate_dict = {}

        for i, letter in enumerate(s):

            if letter in duplicate_dict:
                continue
            if letter not in unique_dict:
                unique_dict[letter] = i
            else:
                del unique_dict[letter]
                duplicate_dict[letter] = i

        if unique_dict:
            return list(unique_dict.values())[0]
        else:
            return -1
