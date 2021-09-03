class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = []
        d = {}
        c = 0
        
        for word in strs:
            
            w = "".join(sorted(word))
            if w not in d:
                d[w] = c
                ans.append([])
                c += 1
            ans[d[w]].append(word)
        
        return ans