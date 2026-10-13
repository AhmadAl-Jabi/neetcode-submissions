from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # input: 2D matrix -1 is water (cannot traverse), 0 is treasure, 2**31 - 1 (INF) is land we can traverse
        # mutate the land cells with the distance to nearest treasure chest --> if impossible it remains INF (don't touch it)
        # traverse vertically or horizontally

        ''' 
        Input
        [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
'''
        '''
        Output
        [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
'''
        # Observations
        # if we're on a land next to a land that isn't inf, then curr value is just smallest of all min(neighbour's + 1)
        # BFS starting from all the chests (multi source BFS) themselves and expand outwards --> mutating the land cells we visit
        # if we visit a land that's already mutated --> another chest must have reached it first (don't mutate)

        # Algorithm
        # We can start by traversing the rows and columns and adding (row,col) of all the chests (0s) we see into a queue
        # Each time we popleft and explore the neighbours of the cell in our queue only if they're an untouched land (INF) --> make sure not out of bounds
        # When we process a cell edit its value to 1 + current_val

        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        queue = deque()
        INF = 2**31 - 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row,col))

        while queue:
            curr_element = queue.popleft()
            row, col = curr_element[0], curr_element[1]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if new_row < 0 or new_col < 0 or new_row >= rows or new_col >= cols or grid[new_row][new_col] != INF:
                    continue
                queue.append((new_row, new_col))
                grid[new_row][new_col] = grid[row][col] + 1
    


















