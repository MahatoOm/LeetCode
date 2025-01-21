class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        m = 2
        n = len(grid[0])
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        minimum_sum = float("inf")
        for turn_index in range(len(grid[0])):
            first_row_sum -= grid[0][turn_index]
            # Find the minimum maximum value out of first_row_sum and
            # second_row_sum.
            minimum_sum = min(minimum_sum, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][turn_index]
        return minimum_sum
            





        # moves to right and down only
        # dir = [(0, 1), (1,0)]

        # heap = []
        # #heap contains sum, x, y , list that stores previous visited cells
        # heapq.heappush(heap, [grid[0][0],0,0,[(0,0)]])
        # paths =[]

        # while heap:
        #     val, x, y, path = heapq.heappop(heap)
        #     if x == 1 and y == n-1:
        #         paths.append(path)

        #     # followinf right and directions
        #     for dx, dy in dir:
        #         nx , ny = x + dx, y + dy
                

        #         if 0<=nx<m and 0<=ny<n and (nx,ny) not in path:
        #             heapq.heappush(heap , [val + grid[nx][ny], nx, ny,path + [(nx,ny)]])



        # print(val)
        # print(path)
        # print(paths , 'll')

        

        

        # results = []
        
        # for i in range(len(paths)):
        #     path = paths[i]
        #     result = 0

        #     #starting for second robot fofr shortest path
        #     heapq.heappush(heap, [0,0,0])
        #     visited = set()
        #     while heap:
        #         val , x, y = heapq.heappop(heap)
        #         if (x,y) in path:
        #             val = 0
                
        #         #checking all directions
        #         for dx, dy in dir:
        #             nx , ny = x+ dx, y+dy

        #             if 0<=nx<m and 0<=ny<n:
        #                 if (nx,ny) in path:
        #                     result = max(result , val + 0) 
        #                     heapq.heappush(heap , [val + 0, nx, ny])
        #                 else:
        #                     result = max(result , val + grid[nx][ny]) 
        #                     heapq.heappush(heap , [val + grid[nx][ny], nx, ny])

        #     print(result,"result")
        #     results.append(result)
        # return min(results)




        
'''
Approach

1. collect all the paths from (0,0) to (1,n-1)
2.  run tha  entire loop for paths as Path
    calculate maxmimin result in that loop considering all propabilities and making checking condition of x,y in path as 0
3. as each loop ends store result in results
4 return min results

'''
