from queue import PriorityQueue

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        q = PriorityQueue()
        
        for point in points:
            x, y = point[0], point[1]
            
            d = (x**2 + y**2)
            
            if q.qsize() < k:
                q.put((-d, [x, y]))
            else:
                dist, pts = q.get()
                if -dist > d:
                    q.put((-d, [x, y]))
                else:
                    q.put((dist, pts))
        
        ans = []
        while q.qsize() > 0:
            dist, pts = q.get()
            ans.append(pts)
            
        return ans
    