class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        counter = 0

        def dfs(row, col):

            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            for direction in directions:
                dfs(row + direction[0], col + direction[1])
        

        # we should iterate over grids and any time we see a "1" we initiate a dfs or bfs on it (imma do dfs)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    counter += 1
                    dfs(i,j)
            
        # return the counter
        return counter

