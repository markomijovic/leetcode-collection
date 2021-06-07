import itertools 
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        if len(digits) == 0:
            return []
        
        d = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        
        if len(digits) == 1:
            return [letter for letter in d[digits[0]]]
        
        my_letters = []
        for num in digits:
            my_letters.append(d[num])
        
        l = list(itertools.product(*my_letters))
        return map(join_tuple_string, l)
    
def join_tuple_string(strings_tuple) -> str:
   return ''.join(strings_tuple)