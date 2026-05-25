import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        n = len(points)
        for i in range(k):
            val = -math.sqrt(points[i][0]**2 + points[i][1]**2)
            heapq.heappush(heap,(val,points[i][0],points[i][1]))
            # print(heap)
        for i in range(k,n):
            val = -math.sqrt(points[i][0]**2 + points[i][1]**2)
            if -heap[0][0]>-val:
                curr = heapq.heappop(heap)
                heapq.heappush(heap,(val,points[i][0],points[i][1]))
        ans = []
        # print(heap)
        while heap:
            curr = heapq.heappop(heap)
            ans.append([curr[1],curr[2]])
        
        return ans


                

        