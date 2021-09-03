class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        self.tar = sys.maxsize
        n = len(nums)
        for i in range(n - 2):
            
            first = nums[i]
            j = i + 1
            k = n - 1
            while (j < k):
                _sum = first + nums[j] + nums[k]
                if _sum == target:
                    return target
                elif _sum > target:
                    k -= 1
                else:
                    j += 1
                if abs(_sum - target) < abs(self.tar - target): 
                    self.tar = _sum
                    
        return self.tar
    