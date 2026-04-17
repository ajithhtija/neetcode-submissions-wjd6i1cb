class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        j = n-2
        dp[n-1] = True
        while j>=0:
            k = 1
            while k<=nums[j] and k+j<n:
                dp[j] = dp[j] or dp[k+j]
                k+=1
            j-=1
        return dp[0]


        