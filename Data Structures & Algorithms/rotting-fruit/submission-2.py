class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Basically start by adding all the rotten fruits to the queue (so look for the ones marked 2)
        # Then we do a bfs where we use queues and queue up all the neighbors that are not rotten and mark them as rotten now
        # Remove the previous guys from the queue. We keep going until the queue is empty and we can return a count for like max min

        # Watch out for:
        # When the queue is empty but there is still a fresh fruit
        # If all the fruit are fresh initially
        # If all the fruit are rotten

        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        queue = []
        fresh_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j)) # we get our initial rotten fruit
                elif grid[i][j] == 1:
                    fresh_count += 1

        def bfs(queue):
            nonlocal fresh_count
            time = -1
            temp_q = []
            
            while True:
                while queue:
                    
                    r,c = queue[0][0], queue[0][1]
                    for dirs in directions:
                        dr, dc = r + dirs[0], c + dirs[1]
                        if (dr<0) or (dc<0) or (dc>=len(grid[0])) or (dr>=len(grid)) or (grid[dr][dc] == 2) or (grid[dr][dc] == 0):
                            continue
                        grid[dr][dc] = 2
                        fresh_count -= 1
                        temp_q.append((dr,dc))
                    queue.pop(0)

                time += 1
                if temp_q:
                    queue = temp_q
                    temp_q = []
                else:
                    return time

        time = bfs(queue)
        if fresh_count > 0:
            return -1
        return time

              






