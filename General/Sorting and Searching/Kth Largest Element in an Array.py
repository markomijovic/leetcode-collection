from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        q = PriorityQueue()
        
        for num in nums:
            q.put(num)
            if q.qsize() > k:
                q.get()
        return q.get()
        
        """O(nlogn)"""
        """
        nums.sort(reverse=True)
        return nums[k-1]
        """