class Solution:
    def isValid(self, s: str) -> bool:
        
        match = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        stack = []
        
        for paren in s:
            if paren == "(" or paren == "[" or paren == "{": 
                stack.append(match[paren])
            else:
                if not stack or paren != stack.pop():
                    return False
        
        return len(stack) == 0