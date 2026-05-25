class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mt = dict()
        ms = dict()
        n = len(s)
        m = len(t)
        if n<m:
            return ""
        for i in s:
            if i not in ms:
                ms[i]=0
            if i not in mt:
                mt[i]=0
        for i in t:
            if i not in ms:
                ms[i] = 0
            if i not in mt:
                mt[i] = 0
            mt[i]+=1
        l = 0
        r = len(t)
        leng  = float("inf")
        ans = ""
        for i in range(l,r):
            ms[s[i]]+=1
        r-=1
        while r<n:
            flag = True
            for key in mt.keys():
                if mt[key]>ms[key]:
                    flag = False
                    break
            if flag:
                if leng>r-l+1:
                    ans = s[l:r+1]
                    leng = r-l+1
                ms[s[l]]-=1
                l+=1
            else:
                r+=1
                if r<n:
                    ms[s[r]]+=1
        return ans
            
            




            
        
        
            

