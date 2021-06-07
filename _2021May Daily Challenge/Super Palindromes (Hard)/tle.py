from math import ceil, sqrt

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        l_int = int(left)
        r_int = int(right)
        ans = []
        perf_squares = self.perfect_squares(l_int, r_int)
        for num in perf_squares:
            if self.is_palindrome(str(num)):
                #print(num) - OK
                if self.is_palindrome(str(int(sqrt(num)))):
                    #print(num) - OK
                    ans.append(num)
        return len(ans)
                
    def perfect_squares(self, lo, hi):
        root = int(math.ceil(lo ** 0.5))
        num = root ** 2
        delta = 2 * root + 1
        while num <= hi:
            yield num
            num += delta
            delta += 2
    
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]