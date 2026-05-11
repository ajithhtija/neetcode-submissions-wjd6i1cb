class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # graph part is constructed 
        vis = set()
        cnt = 0
        def dfs(node):
            if node in vis:
                return 
            vis.add(node)
            for i in adj[node]:
                if i not in vis:
                    dfs(i)
            return 
        for i in range(n):
            if i not in vis:
                dfs(i)
                cnt+=1
        return cnt