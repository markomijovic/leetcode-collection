from queue import PriorityQueue

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals: return 0
        
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = 1
        q = PriorityQueue()
        q.put(intervals[0][1])
        
        for interval in intervals[1:]:
            
            if interval[0] < q.queue[0]: 
                ans += 1 # start time before soonest end time -> need 1 more room
            else: 
                q.get()
            q.put(interval[1])
            
        return ans
            