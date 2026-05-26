class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        temp = []
        ans = []
        def s(index,temp):
            if index==n:
                ans.append(temp[:])
                return 
            temp.append(nums[index])
            s(index+1,temp)
            val = nums[index]
            while index+1<n and val==nums[index+1]:
                index+=1
            temp.pop()
            s(index+1,temp)
        s(0,temp)
        return ans