class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip(' ')
        length = len(s)
        sign = ""
        number = ""
        
        for i, c in enumerate(s):
            if (i == 0) and (c == "+" or c == "-") and (not sign):
                sign = c
                continue
            try:
                digit = int(c)
                number += c
            except:
                break
        
        if len(number) == 0:
            return 0
        
        int_num = int(number)
        if sign == "-":
            int_num *= -1
            if int_num < -2**31:
                return -2**31
        else:
            if int_num > 2**31 - 1:
                return 2**31 - 1
        
        return int_num