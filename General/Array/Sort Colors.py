class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        red = 0
        white = 1
        blue = 2
        """
        p0, p2 = 0, len(nums)-1
        curr = 0
        
        while (curr <= p2):
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2-= 1
            else: curr += 1
            