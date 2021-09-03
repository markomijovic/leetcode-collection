class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        self.ans = []
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return []

        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            j = i + 1
            k = n - 1
            while(j < k):
                second = nums[j]
                third = nums[k]
                _sum = first + second + third
                
                if _sum > 0:
                    k -= 1
                elif _sum < 0:
                    j += 1
                else: # is 0
                    self.ans.append([first, second, third])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        
        return self.ans
    