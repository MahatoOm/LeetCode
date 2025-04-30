class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2)
        p = len(mat2[0])
        res = [[0] * p for _ in range(m)] 
# Matrix multiplication
        for i in range(m):
            for j in range(p):

                for pos in range(k):
                    res[i][j] += (mat1[i][pos] * mat2[pos][j]) 


        return res 