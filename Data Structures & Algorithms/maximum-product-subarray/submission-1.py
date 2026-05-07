class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p = 1
        s = 1
        res = nums[0]
        n = len(nums)
        for i in range(0,n):
            if p==0:
                p=1
            if s==0:
                s=1
            p = p * nums[i]
            s = s * nums[n-i-1]
            res = max(res,max(p,s))
        return res

            
        