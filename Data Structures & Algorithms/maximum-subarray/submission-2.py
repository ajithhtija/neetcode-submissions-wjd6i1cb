class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        maxs = nums[0]
        n = len(nums)
        for i in range(1,n):
            if sum <0 : 
                sum = nums[i]
            else:
                sum = sum + nums[i]
            if sum > maxs:
                maxs = max(maxs,sum)
        return maxs
        