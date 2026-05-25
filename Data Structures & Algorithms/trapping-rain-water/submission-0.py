class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = [0 for _ in range(n)]
        rightmax = [0 for _ in range(n)]   
        lmax = 0     
        for i in range(0,n):
            leftmax[i] = lmax
            lmax = max(lmax,height[i])
        rmax = 0
        for i in range(n-1,-1,-1):
            rightmax[i] = rmax
            rmax = max(rmax,height[i])
        ans = 0
        for i in range(0,n):
            val = min(leftmax[i],rightmax[i])-height[i]
            if val>=0:
                ans+=val
        return ans


            