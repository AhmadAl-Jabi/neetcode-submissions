from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # input: 2D grid containing 0, 1 or 2
        # output: number of minutes elapsed until zero fresh fruits (all 0s or 2s in grid)
        # if impossible return -1

        # 1 <= grid.length, grid[i].length <= 10
        # each minute, any fresh fruit adjacent to rotten fruit will also turn rotten (1 -> 2) (minutes are turns)

        # [1,0,0],
        # [1,2,0],
        # [0,1,2] min = 4

        # [(2,1)]

        # Observations:
        # keep a counter of how many fresh fruits we processed so we can check if there are any left in the end

        # BFS from all the rotten fruits basically --> for a given turn, every rotted fruit rots its neighbours
        # start the BFS from our initially rotten fruits (coords) --> each turn as a minute --> maintain queue (use the initial elements as this turn's elements)
        # process all the elements currently in the queue before incrementing minutes and processing the neighbours next (so on and so forth)
        # when we reach a fresh fruit from a rotten one --> set it to rotten to avoid visiting it again

        # Algorithm:
        # visit all elements and count the initially fresh fruits --> put the rotten ones in our queue
        # while queue (BFS) going over neighbours (if in bounds and fresh), marking them as rotten and then adding to queue
        # increment the minutes for each level
        # if we processed all fresh fruits (fresh_left = 0) then return minutes otherwise return -1

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_left = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_left += 1
                elif grid[row][col] == 2:
                    queue.append((row,col))
        
        minutes = 0
        while queue and fresh_left > 0:
            for i in range(len(queue)):
                curr_element = queue.popleft()
                row, col = curr_element[0], curr_element[1]

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    
                    # if it's out of bounds, already rotted (2), or a 0 we continue (don't append)
                    if new_row < 0 or new_col < 0 or new_row >= rows or new_col >= cols or grid[new_row][new_col] != 1:
                        continue
                    queue.append((new_row,new_col))
                    grid[new_row][new_col] = 2
                    fresh_left -= 1

            minutes += 1

        return minutes if fresh_left == 0 else -1































