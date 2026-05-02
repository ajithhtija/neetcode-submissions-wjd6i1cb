class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,col = len(heights),len(heights[0])
        pac,alt = set(),set()

        def dfs(r,c,visit,prevheight):

            if (r,c) in visit or r<0 or c<0 or r>=rows or c>=col or heights[r][c]<prevheight:
                return 
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for i in range(rows):
            dfs(i,0,pac,heights[i][0])
            dfs(i,col-1,alt,heights[i][col-1])
        for i in range(col):
            dfs(0,i,pac,heights[0][i])
            dfs(rows-1,i,alt,heights[rows-1][i])
        
        res = []
        for i in range(rows):
            for j in range(col):
                if (i,j) in pac and (i,j) in alt :
                    res.append([i,j])
        return res


        