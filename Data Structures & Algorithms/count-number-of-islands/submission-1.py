class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # basically if there is no immediate land left/right or above/below a land then it would count as an island
        self.islands_seen = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
        # we can maybe use a dfs nested func here --> all it does is explore all adjacent nodes (i,j pairs), when it sees 0 returns, or is out of bounds returns, and otherwise when it sees 1 it'll set it as 0 and do dfs on everything near it
            if i < 0 or i == len(grid) or j == len(grid[0]) or j < 0:
                return 
            
            if grid[i][j] == "0":
                return 
            
            # Otherwise if what we saw is a 1 set to 0 explore all its neighbors
            grid[i][j] = "0"
            dfs(i + 1,j)
            dfs(i,j + 1)
            dfs(i - 1,j)
            dfs(i,j - 1)

        # then the way we call that dfs function would be on all rows and colums and only when curr is 1. If so, increase "self.total_islands" += 1 and then run dfs on the node
        for row in range(rows):
            for col in range(cols):
                # if we see a 0 then we don't do anything
                if grid[row][col] == "1":
                    self.islands_seen += 1
                    dfs(row, col)
        
        return self.islands_seen
        


        