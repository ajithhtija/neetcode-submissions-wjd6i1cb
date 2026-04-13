class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key = lambda a: a[0])
        ans.append(intervals[0])
        n = len(intervals)
        for i in range(1,n):
            if ans[-1][1]<intervals[i][0]:
                ans.append(intervals[i])
            else:
                l = ans.pop()
                ans.append([l[0],max(l[1],intervals[i][1])])
        return ans