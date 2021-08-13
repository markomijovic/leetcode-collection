"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        ans = []
        c = 0  # placement counter for the 2d list
        for word in strs:
            w = "".join(sorted(word))

            if w not in anagrams:
                anagrams[w] = c
                ans.append([])
                ans[c].append(word)
                c += 1
            else:
                idx = anagrams[w]
                ans[idx].append(word)
        return ans
