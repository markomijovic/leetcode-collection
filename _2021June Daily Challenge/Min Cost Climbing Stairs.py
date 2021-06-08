"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        f = [0] * len(cost)
        f[0], f[1] = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            f[i] = cost[i] + min(f[i - 1], f[i - 2])
        return min(f[-1], f[-2])