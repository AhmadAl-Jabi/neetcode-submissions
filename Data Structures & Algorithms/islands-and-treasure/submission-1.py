from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # we can do a normal bfs approach where we scan entire grid starting from treasure and only update when the land we hit either has inf value or its value is bigger than parent + 1.
        queue = deque()

        # However this can be even more optimal with multi-source bfs instead
        # Basically one pass the entire grid and queue up all (row,col) pairs of treasures
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row,col))
        # Then while queue we basically popleft, check its children (store left,right,up,down):

        # if out of bound ignore
        # if its a water we just ignore it
        # if its a touched land we just ignore it
        # if its a treasure we ignore it
        # if untouched land (still has inf) then set its value to curr + 1 and append to queue
        while queue:
            curr = queue.popleft() # (row_c,col_c) tuple
            row_c, col_c = curr[0], curr[1]
            
            left = (row_c - 1, col_c)
            right = (row_c + 1, col_c)
            up = (row_c, col_c + 1)
            down = (row_c, col_c - 1)

            for direction in [left, right, up, down]:
                row, col = direction[0], direction[1]

                if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != (2**31 - 1):
                    continue
                # if proper land then set its value to parent + 1    
                grid[row][col] = grid[row_c][col_c] + 1
                queue.append((row,col))

        # set the current land's value to 1 + parent's value

        
        