class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        

        m = len(grid)
        grid_list = [] 
        for i in range(m):
            grid_list += grid[i]

        
        grid_list.sort()
        n = len(grid_list)
        # print(grid_list)

        
        median = grid_list[n//2]
        count = 0
        for i in range(n):
            element = grid_list[i]
            if abs( median - element) % x != 0:
                return -1
            needed_count = abs(median - element )/ x
            count += needed_count




        return int(count)