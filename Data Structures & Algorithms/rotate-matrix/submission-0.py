class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(0,n):
            for j in range(i+1,n):
                k = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = k
            matrix[i] = matrix[i][::-1]
        return  
        