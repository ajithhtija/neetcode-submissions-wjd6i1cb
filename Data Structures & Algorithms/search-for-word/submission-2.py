class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        vis = set()
        def dfs(i,j,w):

            if w==len(word):
                return True
            if i<0 or j<0 or j>=n or i>=m or (i,j) in vis:
                return False
            if board[i][j]!=word[w]:
                return False
            vis.add((i,j))
            kids = [[0,1],[0,-1],[1,0],[-1,0]]

            for u,v in kids:
                if dfs(i+u,j+v,w+1):
                    return True
            vis.remove((i,j))
            return False
        for p in range(m):
            for q in range(n):
                if dfs(p,q,0):
                    return True
        return False
        
            



        