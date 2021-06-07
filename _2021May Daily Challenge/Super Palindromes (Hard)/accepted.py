class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        ans = []
        l_int = int(left)
        r_int = int(right)
        # idea: can construct all 9 digit (9^2 = 18) palindromes
        # with 4 digits total iea abcd|dcba plus abcd|X|dcba
        palindromes = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(1, 10000):
            s1 = str(i) + str(i)[::-1]
            palindromes.append(s1)
            for j in range(0, 10):
                s2 = str(i) + str(j) + str(i)[::-1]
                palindromes.append(s2)
        palindromes = list(map(int, palindromes))
        palindromes.sort()
        
        for palindrome in palindromes:
            p = palindrome**2
            if p > r_int:
                break
            if p < l_int:
                continue
            if is_palindrome(str(p)):
                ans.append(p)
        return len(ans)
    
def is_palindrome(s: str) -> bool:
    return s == s[::-1]