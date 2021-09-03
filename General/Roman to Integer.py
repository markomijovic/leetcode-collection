class Solution:
    def romanToInt(self, s: str) -> int:
        
        self.ans = 0
        d = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        c = len(s) - 1
        while (c >= 0):
            if c >= 1:
                if s[c-1] + s[c] in d:
                    self.ans += d[s[c-1] + s[c]]
                    c -= 2
                    continue
            if s[c] in d:
                self.ans += d[s[c]]
                c -= 1
                
        return self.ans
                