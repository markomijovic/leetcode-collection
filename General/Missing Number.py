class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.sort()
        if nums[0] != 0:
            return 0
        
        for i in range(n-1):
            
            if nums[i] + 1 != nums[i + 1]:
                return nums[i] + 1
        
        return n

"""class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number"""