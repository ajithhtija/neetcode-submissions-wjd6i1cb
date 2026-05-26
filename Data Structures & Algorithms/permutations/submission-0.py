class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def p(nums,index,n):

            if index==n-1:
                ans.append(nums[:])
                return 

            for i in range(index,n):
                nums[index],nums[i] = nums[i],nums[index]
                p(nums,index+1,n)
                nums[index],nums[i] = nums[i],nums[index]
        p(nums,0,n)
        return ans
        