import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = set()
        # visited = [[False] * n for _ in range(m)]
        heap = []

        # Push all border cells into the heap
        for i in range(m):
            for j in [0, n - 1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited.add((i,j))


        # print(heap)
        # print(visited)
        for j in range(n):
            for i in [0, m - 1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                # visited[i][j] = True
                visited.add((i,j))

                # print(i,j)
        # print(heap)
        # print(visited)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        trapped_water = 0

        while heap:
            height, x, y = heapq.heappop(heap)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited:
                    trapped_water += max(0, height - heightMap[nx][ny])
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                    # visited[nx][ny] = True
                    visited.add((nx,ny))

        # print(visited)

        return trapped_water

