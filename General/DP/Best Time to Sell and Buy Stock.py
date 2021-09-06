class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        _min = math.inf
        
        for num in prices:
            if num < _min: _min = num
            max_profit = max(num - _min, max_profit)
                
        return max_profit
                