class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = heights[0]
        for i in range(n):
            length = heights[i]
            width = 1
            left = i-1
            while left>=0 and heights[left]>=heights[i]:
                left-=1
                width+=1
            right = i+1
            while right<n and heights[right]>=heights[i]:
                width+=1
                right+=1
            ans = max(ans,length*width)
        return ans
        