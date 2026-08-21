class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        s= len(grid) 
        cs = len(grid[0]) 
        directions = [[0,1],[1,0],[-1,0],[0,-1]] 
        islands = 0
        
        def dfs(r,c): 
            if ((r<0) or (c>=cs) or (r>=s) or (c<0) or (grid[r][c] == "0") ):
                return 0

            if grid[r][c] == "1":
                grid[r][c] = "0"
                
                for dir in directions:
                    dfs(r + dir[0], c + dir[1])
            return 1
        
        # To make it more optimal we can even just do dfs when it's a 1 at curr pos, but regardless it's fine cuz we return right away if 0
        for i in range(s):
            for j in range(cs):
                islands += dfs(i,j) 
        
        return islands