class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row = [False] * len(matrix)
        column = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range((len(matrix[0]))):

                if matrix[i][j] == 0 :

                    row[i] = True
                    column[j] = True

        
        for r in range(len(row)):
            if row[r]:
                for i in range(len(matrix[0])):
                    matrix[r][i] = 0

        for c in range(len(column)):
            if column[c]:
                for i in range(len(matrix)):
                    matrix[i][c] = 0
            
