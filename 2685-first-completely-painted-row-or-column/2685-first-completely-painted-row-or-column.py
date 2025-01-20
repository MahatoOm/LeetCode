from collections import defaultdict
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        m = len(mat)
        n = len(mat[0])

        #for checking each row 
        painted_row = [[False] * n for _ in range(m)]

        #for checking each column
        painted_column = [[False] * m for _ in range(n)]

        #STORING data as dictionary key and (i, j) as value
        # using dictionary to access data with constant Time complexity O(1).
        matrix_dict = defaultdict(list)
        for i in range(m):
            for j in range(n):
                matrix_dict[mat[i][j]] = [i,j]


        #run all data in arr[k]
        
        for k in range(len(arr)):
            #get pos of arr[k] from dictionart that we created
            i , j = matrix_dict[arr[k]]

            #make row pos True
            painted_row[i][j] = True
            #make col pos True
            painted_column[j][i] = True


            #check if any row or col contains all True means no false in it then return arr[k]
            if False not in painted_row[i] or False not in painted_column[j]:
                return k
            
            

