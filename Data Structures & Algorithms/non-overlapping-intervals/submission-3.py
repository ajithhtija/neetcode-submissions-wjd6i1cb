class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort()
        prevend = intervals[0][1]
        n = len(intervals)
        for start,end in intervals[1:]:
            if start>=prevend:
                prevend = end 
            else:
                ans+=1
                prevend = min(end,prevend)
        return ans

        return 0
        