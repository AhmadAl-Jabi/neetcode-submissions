from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        max_time = 0
        fresh = 0 # keep a counter of initial fresh. If less than this become rotten we return -1 in the end (cuz some were unreachable)

        # we can do multi source bfs were first pass we find as many rotten fruits
        # then we queue them up to our deque
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col,0)) # row,col,time
                elif grid[row][col] == 1:
                    fresh += 1

        # check left, right, up, down
        while queue:
            current = queue.popleft()
            row_c, col_c, minute = current[0], current[1], current[2]
            max_time = max(minute,max_time)

            left_dir = (row_c - 1, col_c, minute + 1)
            right_dir = (row_c + 1, col_c, minute + 1)
            up_dir = (row_c, col_c + 1, minute + 1)
            down_dir = (row_c, col_c - 1, minute + 1)

            for direction in [left_dir,right_dir,up_dir,down_dir]:
                row, col = direction[0], direction[1]
                if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
                    continue
                queue.append(direction) # includes the minute
                grid[row][col] = 2
                fresh -= 1
        
        # if fresh aint 0 we return -1
        return max_time if not fresh else -1
                
                

        # from there if the neighbour is out of bounds, an empty cell or a rotten fruit then we ignore them

        # otherwise we queue up the neighbour with minute + 1 and set it rotten
        # update max time if curr minute bigger

        # the only thing I'm not sure about is how to count the minutes
        