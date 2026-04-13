class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        findme = set()
        ans = 0
        for i in nums:
            if i not in findme:
                findme.add(i)
            else:
                continue 
        for i in nums:
            ##check this i can be a start of the sequence or not 
            ##we can do that by checking if its has a left neighbour or not 
            if (i-1) not in findme:
                cnt = 1
                k = i
                while k+1 in findme:
                    cnt+=1
                    k+=1
                ans = max(ans,cnt)
            else:
                continue 
        return ans 