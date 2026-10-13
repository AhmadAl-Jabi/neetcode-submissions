class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # now we want the maximum area of an island instead -> if no island exists return 0
        # Problem/Assumptions:
        # '1' = land, '0' = water
        # could be rectangular
        # 1 <= grid.length, grid[i].length <= 100
        '''
        [0,0,0,0,1],
        [0,1,0,1,1],
        [1,0,1,1,1]
        output = 3
        '''
        # Observations:
        # Every island has at least one land cell
        # probably want to mark land cells as visited so we avoid visitng them again --> This applies for either dfs or bfs (mark by changing a 1 to a 0)

        # Algorithm:
        # Scan the grid once and anytime we encounter a 1 we can use DFS to go to all the neighbour lands and mark visited so we don't visit again
        # This would count as one big island --> can increment num_islands
        # return num_islands in the end
        # keep doing until we've visited every land (we only visit each land at most once)

        # Code:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        max_area = 0

        # This dfs would only be called on land cells
        def dfs(row,col):
            # base cases
            # if out of bounds or a water cell then we return
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return 0
            # mark the cell as visited
            grid[row][col] = 0
            area = 1
            # go and visit the neighbours
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                area += dfs(new_row, new_col)

            # return area so far
            return area # for the next caller
        
        # need a way of calling dfs
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area,dfs(row,col))

        return max_area

        # FOLLOW UP: Area of an island is just the number of cells within an island
        # We want max area of an island in grid instead of count now
        # We will still use the dfs approach --> Now just need to track the number of islands within a path (the sum is the area)








