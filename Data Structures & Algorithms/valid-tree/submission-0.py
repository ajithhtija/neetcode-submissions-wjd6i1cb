class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # more than n-1 edges indicates cycle in a graph
        if len(edges)>(n-1):
            return False
        vis = set()
        adj = [[] for _ in range(n)]
        #building the undirected graph
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node,parent):
            if node in vis:
                return False
            vis.add(node)
            for k in adj[node]:
                if k==parent:
                    continue
                if not dfs(k,node):
                    return False
            return True 
        
        return dfs(0,-1) and len(vis)==n