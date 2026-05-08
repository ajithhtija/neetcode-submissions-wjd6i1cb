class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            if i not in mp:
                mp[i] = []
            mp[i].append(j)
        vis = set()
        def dfs(c):
            if c in vis:
                return False
            if mp[c]==[]:
                return True
            vis.add(c)
            for i in mp[c]:
                if not dfs(i):
                    return False
            vis.remove(c)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        