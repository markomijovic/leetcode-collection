class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        lexic = []
        digit = []
        
        for log in logs:
            
            # if digit just add to digit[] and continue
            if log[-1].isnumeric():
                digit.append(log)
                continue
            
            # if lexicon have to sort
            lexic.append(log)
        lexic = sorted(lexic, key=lambda x: (x.split(' ')[1:], x.split(" ")[0]))
        
        return lexic + digit
    