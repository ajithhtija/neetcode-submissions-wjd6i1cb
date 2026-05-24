class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m>n:
            return False
        s2mp = [0 for _ in range(26)]
        s1mp = [0 for _ in range(26)]
        for j in range(0,m):
            s2mp[ord(s2[j])-ord('a')]+=1
            s1mp[ord(s1[j])-ord('a')]+=1
        for i in range(m-1,n):
            # compare two maps
            flag = True
            for x in range(26):
                if s1mp[x]!=s2mp[x]:
                    flag = False
                    break
            if flag:
                return flag
            s2mp[ord(s2[i-m+1])-ord('a')]-=1
            if i+1<n:
                s2mp[ord(s2[i+1])-ord('a')]+=1
        
        return False
             

        