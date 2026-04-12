class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        interval = []
        n = len(intervals)
        f = False
        for i in intervals:
            if f==True or i[0]<newInterval[0]:
                interval.append(i)
            elif i[0]==newInterval[0] and i[1]<newInterval[1]:
                interval.append(i)
            elif i[0]==newInterval[0] and i[1]>newInterval[1]:
                interval.append(newInterval)
                interval.append(i)
                f = True
            else:
                interval.append(newInterval)
                interval.append(i)
                f = True
        if f==False:
            interval.append(newInterval)
        # print(interval)
        ans.append(interval[0])
        for p in range(1,n+1):
            if ans[-1][1]<interval[p][0]:
                ans.append(interval[p])
            else:
                l = ans.pop()
                ans.append([l[0],max(l[1],interval[p][1])])
        return ans




        