from typing import List
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # store the (i,j) position in its row pos
        row_count=[[] for _ in range(m) ]
        # store the (i,j) position in its column pos
        column_count = [[] for _ in range(n)]

        print(column_count)

        # rul a loop through all element and chech if it has 1 then push to row or column
        for i in range(m):
            
            for j in range(n):
                if grid[i][j] ==1:
                    row_count[i].append((i,j))
                    column_count[j].append((i,j))

        # counting unique position to each cell in visited
        i , j =0,0
        count = 0
        visited = set()
        while i < m or j < n:
            if i < m and j < n and len(row_count[i]) >=2 and len(column_count[j]) >= 2:
                
                for data in row_count[i]:
                    visited.add(data)
                for data in column_count[j]:
                    visited.add(data)
            
                
            elif i < m and len(row_count[i]) >=2:
             
                
                count = count 
                for data in row_count[i]:
                    visited.add(data)

            elif  j < n and len(column_count[j]) >= 2:

                count = count 
                for data in column_count[j]:
                    visited.add(data)
            i +=1
            j +=1
        # print(row_count)
        # print(column_count)
        # print(visited , "visited")

        return len(visited)