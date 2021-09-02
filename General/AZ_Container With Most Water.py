class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        self.area = 0
        left, right = 0, len(height) - 1
        
        while (left < right):
            
            h = min(height[left], height[right])
            self.area = max(self.area, (right - left) * h)
            if (height[left] >= height[right]):
                right -= 1
            else:
                left += 1
        
        return self.area