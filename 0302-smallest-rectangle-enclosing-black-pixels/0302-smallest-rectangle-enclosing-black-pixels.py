class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        def DFS(X,Y, Row, Col):

            if X < 0 or Y < 0 or X >= Row or Y >= Col or image[X][Y] == "0":
                return
            image[X][Y] = "0"
            self.top = min(self.top, X) 
            self.bottom = max(self.bottom, X + 1)   
            self.left = min(self.left ,Y)
            self.right = max(self.right, Y + 1)

            DFS(X + 1, Y , Row , Col)
            DFS(X - 1, Y , Row , Col)
            DFS(X, Y + 1, Row , Col)
            DFS(X, Y - 1, Row , Col)

        self.top = x
        self.bottom = x
        self.left = y
        self.right = y
        DFS(x, y , len(image) , len(image[0]))
        return (self.right- self.left) * (self.bottom - self.top)
  
'''
# Using heap tle     
        x_set = set()
        y_set = set()

        heap = []
        heapq.heappush(heap, (x,y))
        # heap.append((x,y))
        visited = set()
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        while heap:
            i , j = heapq.heappop(heap)
            image[i][j] = 0
            visited.add((i,j))
            x_set.add(i)
            y_set.add(j)

            for dx, dy in dir:
                nx, ny = i + dx, j + dy

                if 0 <= nx < len(image) and 0 <= ny < len(image[0]) and (nx,ny) not in visited and image[nx][ny] == "1":
                    heapq.heappush(heap, (nx, ny))


        return len(x_set) * len(y_set)


'''

            