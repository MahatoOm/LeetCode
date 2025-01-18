class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        heap = []
        visited = set()

        heapq.heappush(heap, [0,0,0])
        output  = []
        while heap:

            cost, i , j  = heapq.heappop(heap)

            if i < 0 or j < 0 or i > m-1 or j > n-1:
                continue
            if i == m-1 and  j == n-1:
                return cost
                

            if (i,j)  in visited:
                continue
            visited.add((i,j))


            val = grid[i][j]
            if val == 1:
                heapq.heappush(heap, [cost, i, j+1, ])
                heapq.heappush(heap, [cost+1 , i, j-1])
                heapq.heappush(heap, [cost+1, i+1, j])
                heapq.heappush(heap, [ cost+1, i-1, j])

            elif val == 2:
                heapq.heappush(heap,[cost ,i, j-1])

                heapq.heappush(heap, [cost+1 , i, j+1])
                heapq.heappush(heap, [cost+1 , i+1, j])
                heapq.heappush(heap, [cost+1 , i-1, j])
            elif val == 3:
                heapq.heappush(heap, [cost, i+1, j])

                heapq.heappush(heap, [cost+1 , i, j-1])
                heapq.heappush(heap, [cost + 1, i, j+1])
                heapq.heappush(heap, [cost + 1, i-1, j])
            else:
                heapq.heappush(heap, [cost , i-1, j])
                heapq.heappush(heap, [cost+1 , i, j-1])
                heapq.heappush(heap, [cost+1 , i+1, j])
                heapq.heappush(heap, [cost+1, i, j+1])


        

