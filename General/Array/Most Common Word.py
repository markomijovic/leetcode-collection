class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        n = len(paragraph)
        banned = set(banned)
        d = {}
        ans = ["", 0]
        word_buffer = []
        for i, char in enumerate(paragraph):
            
            if char.isalnum():
                word_buffer.append(char.lower())
                if i != n - 1:
                    continue
            
            if len(word_buffer) > 0:
                word = "".join(word_buffer)
                if word not in banned:
                    if word not in d:
                        d[word] = 1
                    else:
                        d[word] += 1
                    if d[word] > ans[1]:
                        ans[0], ans[1] = word, d[word]
            
            word_buffer = []
            
        return ans[0]