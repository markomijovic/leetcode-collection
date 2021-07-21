"""
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

    Solution(int[] nums) Initializes the object with the integer array nums.
    int[] reset() Resets the array to its original configuration and returns it.
    int[] shuffle() Returns a random shuffling of the array.
"""

class Solution:
    
    def __init__(self, nums):
        self.arr = nums
        self.original = list(nums)

    def reset(self):
        self.arr = self.original
        self.original = list(self.original) # reseting pointer
        return self.arr

    def shuffle(self):
        for i in range(len(self.arr)):
            swap_idx = random.randrange(i, len(self.arr))
            self.arr[i], self.arr[swap_idx] = self.arr[swap_idx], self.arr[i]
        return self.arr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()