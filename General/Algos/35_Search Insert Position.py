class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0

        left, right = 0, len(nums) - 1

        while (left <= right):

            mid = (left + right) // 2

            if (nums[mid] == target):
                return mid
            elif (target > nums[mid]):
                left = mid + 1
                if (target < nums[left]):
                    return left
            else:
                right = mid - 1
                if (target > nums[right]):
                    return mid
