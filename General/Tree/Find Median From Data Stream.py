from queue import PriorityQueue

class MedianFinder:
    
    def __init__(self):
        self.lo = PriorityQueue()
        self.hi = PriorityQueue()
        
    def addNum(self, num: int) -> None:
        self.lo.put(-num)
        maxLo = -1*self.lo.get()
        self.hi.put(maxLo)
        
        if (self.lo.qsize() < self.hi.qsize()):
            self.lo.put(-1*self.hi.get())

    def findMedian(self) -> float:
        if self.lo.qsize() > self.hi.qsize():
            median = self.lo.get()
            self.lo.put(median)
            return -1*median
        else:
            medianR = self.hi.get()
            medianL = self.lo.get()
            self.hi.put(medianR)
            self.lo.put(medianL)
            return (medianR + -1*medianL) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()