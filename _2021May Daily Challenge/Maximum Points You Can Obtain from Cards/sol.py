class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_pts = sum(cardPoints)
        n = len(cardPoints)
        if k == n:
            return total_pts
        ans = total_pts-sum(cardPoints[0:n-k])
        s = ans
        for i in range(k):
            s = s - cardPoints[n-k+i] + cardPoints[i]
            if s > ans:
                ans = s
        return ans