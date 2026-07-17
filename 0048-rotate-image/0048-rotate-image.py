class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(matrix)//2):
            matrix[i],matrix[-(i+1)] = matrix[-(i+1)],matrix[i]
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])-1):
                matrix[i][j+1],matrix[j+1][i] = matrix[j+1][i],matrix[i][j+1]
        return 
        