class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        m = len(grid)
        n = len(grid[0])

        k = len(queries)

        queries_heap = []
        for i in range(k):
            heapq.heappush(queries_heap, (queries[i], i))
        print(queries_heap)



        res = [0] * k
        count = 0
        extra = [(grid[0][0], 0, 0)]
        visited = set()
        dir = [(0,1), (0,-1), (1,0), (-1, 0)]

        for i in range(k):

            comp_point, pos = heapq.heappop(queries_heap)
            heap = []
            while extra and extra[0][0] < comp_point:
                heapq.heappush(heap, (heapq.heappop(extra)))

            while heap:

                curr_point , x, y = heapq.heappop(heap)
                if (x,y) in visited:
                    continue
                
                visited.add((x,y))
                if comp_point > curr_point:
                    count +=1
                    for dx , dy in dir:

                        nx, ny = x + dx , y+ dy

                        if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited:
                            if grid[nx][ny] < comp_point  :
                                heapq.heappush(heap, (grid[nx][ny], nx, ny))
                            else:
                                heapq.heappush(extra, (grid[nx][ny], nx, ny ))

            res[pos] = count             
        return res