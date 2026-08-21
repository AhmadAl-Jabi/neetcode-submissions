class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Basically the difference here is that when we loop over the 4 diff directions
        # Each one should return a 1 if it hit an island and a 0 if it didn't
        # If none hit an island we just return whatever the curr counter was
        # If a call hits a ground, it sets that ground to 0 (so we don't duplicate count)

        # If curr is ground, we set count = 1 and then we do count + dfs(dir) for each dir
        # And after the for loop we just return count as a whole. This worksf or dfs since we build up the counter till the end

        rows = len(grid) 
        cols = len(grid[0]) 

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(r, c):
            if ((r<0) or (c<0) or (r>=rows) or (c>=cols) or grid[r][c] == 0):
                return 0

            grid[r][c] = 0
            count = 1

            for dirs in directions:
                count += dfs(r + dirs[0], c + dirs[1])

            return count
        
        max_count = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:
                    
                    curr_count = dfs(i,j)
                    if curr_count > max_count:
                        max_count = curr_count
        
        return max_count
                    
        