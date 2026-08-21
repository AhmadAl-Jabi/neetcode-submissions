class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        # The approach I'm thinking is very similar to counting islands except now we'll have a nonlocal max_area that we check curr_area against for each node
        def dfs(row,col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0 # count of a null node is 0
            
            if grid[row][col] == 0:
                return 0 # count of a 0 is 0
            
            # set the curr node to a zero BEFORE traversing to avoid inf loop
            grid[row][col] = 0
            # 1 + the amount of all neighbours (1 is the curr node)
            curr_count = 1 + dfs(row + 1,col) + dfs(row - 1,col) + dfs(row,col + 1) + dfs(row,col -1)

            self.max_area = max(curr_count,self.max_area)
            return curr_count
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]: # if 1 evaluates to true 
                    dfs(row,col)
                    
        return self.max_area


        