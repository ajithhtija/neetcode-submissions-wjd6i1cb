class MedianFinder:

    def __init__(self):
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        if self.maxh and num > -1*self.maxh[0]:
            heapq.heappush(self.minh,num)
        else:
            heapq.heappush(self.maxh,-1*num)
        if len(self.minh)>len(self.maxh)+1:
            val = heapq.heappop(self.minh)
            heapq.heappush(self.maxh,-1*val)
        if len(self.maxh)>len(self.minh)+1:
            val = heapq.heappop(self.maxh)
            heapq.heappush(self.minh,-1*val)
        
    def findMedian(self) -> float:
        if len(self.maxh)>len(self.minh):
            return -1*self.maxh[0]
        elif len(self.maxh)<len(self.minh):
            return self.minh[0]
        else:
            return (-1*self.maxh[0] + self.minh[0])/2
        
        