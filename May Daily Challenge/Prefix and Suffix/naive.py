class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.index = -1

    def f(self, prefix: str, suffix: str) -> int:
        
        for i in range(len(self.words)-1, -1, -1):
            word = self.words[i]
            if (word.startswith(prefix) and word.endswith(suffix)):
                return i
        return self.index


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)