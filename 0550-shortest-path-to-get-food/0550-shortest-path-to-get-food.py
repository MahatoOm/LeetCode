class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        # Find position of the person ('*') in the grid
        man_pos = []
        for i in range(len(grid)):  # Iterate through each row
            if "*" in grid[i]: 
             # Check if '*' is in the current row
                j = grid[i].index("*")  # Get the column index of '*'
                man_pos = [(i, j)]  # Store the position as a tuple
                break  # Exit the loop once the position is found

        # Initialize a min-heap for BFS, starting with the person's position
        heap = []
        heapq.heappush(heap, [0, man_pos[0][0], man_pos[0][1]])  # [distance, row, col]

        # Define possible movement directions (right, left, down, up)
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Track visited positions to prevent re-visiting
        visited = set()
        visited.add((man_pos[0][0], man_pos[0][1]))

        # Perform BFS
        while heap:
            dis, x, y = heapq.heappop(heap)  # Get the current position with the smallest distance

            for dx, dy in dir:  # Check all possible directions
                nx, ny = x + dx, y + dy  # Calculate new position

                # Ensure the new position is within grid bounds
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):   
                    if grid[nx][ny] == '#':  # Check if the current position is food
                        return dis + 1  # Return the distance to food

                    # If the position is open ('O') and not visited, add it to the heap
                    if grid[nx][ny] == "O" and (nx, ny) not in visited:
                        visited.add((nx, ny))  # Mark the position as visited
                        heapq.heappush(heap, [dis + 1, nx, ny])  # Add to heap with updated distance

        return -1  # Return -1 if food is not reachable
