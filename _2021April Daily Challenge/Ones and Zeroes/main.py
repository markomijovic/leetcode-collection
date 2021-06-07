class Solution:
    def findMaxForm(self, strs: List[str], M: int, N: int) -> int:
        
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for str in strs:
            zeros = str.count("0")
            ones = len(str) - zeros
            for i in range(M, zeros - 1, -1):
                for j in range(N, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[M][N]