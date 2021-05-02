class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.index = -1
        
class Trie(object):
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, index):
        node = self.root
        node.index = index
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.index = index
        
            
    def search(self, prefix, suffix):
        p_s = suffix+"#"+prefix
        node = self.root
        for char in p_s:
            if char not in node.children:
                return -1
            node = node.children[char]
        return node.index


class WordFilter:

    def __init__(self, words: List[str]):
        self.tr = Trie()
        for indx, word in enumerate(words):
            N = len(word)
            t = word+"#"+word
            for i in range(N):
                self.tr.insert(t[i:], indx)
        
    def f(self, prefix: str, suffix: str) -> int:
        
        return self.tr.search(prefix, suffix)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)