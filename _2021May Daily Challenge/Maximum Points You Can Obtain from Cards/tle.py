class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_pts = sum(cardPoints)
        n = len(cardPoints)
        if k == n:
            return total_pts
        temp = cardPoints[0:n-k]
        ans = total_pts-sum(temp)
        i = 0
        while (n-k+i) < n:
            temp.pop(0)
            temp.append(cardPoints[n-k+i])
            s = total_pts-sum(temp)
            if s > ans:
                ans = s
            i += 1
        return ans