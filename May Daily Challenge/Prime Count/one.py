from math import ceil, sqrt
# from https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        A = [1]*n
        A[0] = A[1] = 0
        for i in range(2, n):
            if A[i]:
                for j in range(2*i, n, i):
                    A[j] = 0
        return sum(A)