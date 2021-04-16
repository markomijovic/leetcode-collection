class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        first = 1
        second = 1
        
        for i in range(2, n):
            temp = first
            first = second
            second = temp + second
        
        return second