class Solution:
    def intToRoman(self, num: int) -> str:
        
        self.ans = []
        
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        for val, symbol in digits:
            
            x, num = divmod(num, val)
            self.ans.append(x*symbol)
        
            
        return "".join(self.ans)