class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        ans = []
        candidates.sort()
        n = len(candidates)
        def ComSum(target,index,temp,n):
            if target==0:
                ans.append(temp[:])
                return 
            if index==len(candidates):
                return 
            if target<0:
                return 
            temp.append(candidates[index])
            ComSum(target-candidates[index],index+1,temp,n)
            val = candidates[index]
            while index+1<n and val==candidates[index+1]:
                index+=1
            temp.pop()
            ComSum(target,index+1,temp,n)

        ComSum(target,0,temp,n)
        return ans
        