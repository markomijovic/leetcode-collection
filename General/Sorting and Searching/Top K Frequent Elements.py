from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        q = PriorityQueue()
        
        count = collections.Counter(nums)
        
        for num in count:
            
            if q.qsize() < k:
                q.put((count[num], num))
            else:
                c, v = q.get()
                if c < count[num]:
                    q.put((count[num], num))
                else:
                    q.put((c, v))
        
        ans = []
        while(q.qsize() > 0):
            c, v = q.get()
            ans.append(v)
        return ans
    