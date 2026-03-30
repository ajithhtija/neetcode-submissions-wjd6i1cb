class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0,r):
            f = False
            for j in range(0,c):
                if matrix[i][j]==0:
                    f = True
                    break
            if f:
                for j in range(0,c):
                    if matrix[i][j]!=0:
                        matrix[i][j] = 9999999999
                    else:
                        continue
        for i in range(0,c):
            f = False
            for j in range(0,r):
                if matrix[j][i]==0:
                    f = True
                    break
            if f:
                for j in range(0,r):
                    if matrix[j][i]!=0:
                        matrix[j][i] = 9999999999
                    else:
                        continue
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j]==9999999999:
                    matrix[i][j] = 0
        


        