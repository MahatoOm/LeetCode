class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])

        #assinnging new matrix heightMatrix with samme row and column
        heightMatrix = [[False] * n for _ in range(m)]

        #heap to access small height first
        heap = []

        #set to not reback to same position to keep track of visited cell
        visited = set()

        # print(heightMatrix)
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:

                    heightMatrix[i][j] = 0
                    heapq.heappush(heap, [0,i,j]) # [height, i, j]
                    visited.add((i,j))

        #checking all possible direction
        direction  = [(0,1), (0,-1), (1,0), (-1,0)]

        #BFS chechiing level by level smallest height first
        while heap:
            height , x, y = heapq.heappop(heap)

            for dx, dy in direction:
                nx , ny = x + dx , y + dy

                if 0 <= nx < m and 0<= ny < n :

                    if (nx, ny) not in visited:
                        heapq.heappush(heap, [height+1, nx,ny])
                        visited.add((nx,ny))
                        heightMatrix[nx][ny] = height+1



        return heightMatrix







