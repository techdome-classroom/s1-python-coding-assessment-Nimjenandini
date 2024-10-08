class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0

        def dfs(grid, i, j):
            # If out of bounds or water, return
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
                return
            # Mark the current land as visited by changing it to water
            grid[i][j] = 'W'
            # Explore the adjacent cells (up, down, left, right)
            dfs(grid, i-1, j)  # Up
            dfs(grid, i+1, j)  # Down
            dfs(grid, i, j-1)  # Left
            dfs(grid, i, j+1)  # Right

        island_count = 0
        
        # Traverse the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':  # Found an unvisited landmass
                    dfs(grid, i, j)    # Explore the entire island
                    island_count += 1  # Increment island count

        return island_count

                    
        return 0
