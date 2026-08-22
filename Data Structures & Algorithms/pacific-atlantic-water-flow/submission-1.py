from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # Define Pacific as row < 0 or col < 0, Atlantic as row >= len(heights) or col >= len(heights[0]) (doesn't matter tbh)
        # basically for our appraoch we need, for a given node, that at least one path exists to Pacific and to Atlantic edges where every other node is smaller. Otherwise it doesn't count

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        pacific_seen, atlantic_seen = set(), set() # sets of tuples (the indices)
        pacific_arr, atlantic_arr = deque(), deque()
        # make a candidate arr of pacific nodes (everything in row[0] and everything in each row col[0])
        for j in range(len(heights[0])):
            pacific_arr.append((0,j))
            pacific_seen.add((0,j))
        for i in range(len(heights)):
            pacific_arr.append((i,0))
            pacific_seen.add((i,0))

        # make a candidate arr of atlantic nodes (everything in row[-1] and everything in each row col[-1])
        for j in range(len(heights[0])):
            atlantic_arr.append((len(heights) - 1,j))
            atlantic_seen.add((len(heights) - 1,j))
        for i in range(len(heights)):
            atlantic_arr.append((i,len(heights[0]) -1))
            atlantic_seen.add((i,len(heights[0]) -1))


        # start from edge nodes (confirmed to be valid nodes)
        # going to use a deque with everything from pacific/atlantic initially
        # multisource bfs so just give it the queue
        def bfs(queue, is_pacific):
            curr_set = pacific_seen if is_pacific else atlantic_seen

            while queue:
                row, col = queue.popleft()
                #curr_set.add((row,col))

                # when we check the neighbours (dirs) we'll make sure that they aren't out of bounds, aren't smaller than curr and aren't in the seen set
                for direction in dirs:
                    dr, dc = row + direction[0], col + direction[1]

                    if dr < 0 or dc < 0 or dr >= len(heights) or dc >= len(heights[0]) or heights[dr][dc] < heights[row][col] or (dr,dc) in curr_set:
                        continue
                    
                    queue.append((dr, dc))
                    curr_set.add((dr,dc))
        
        bfs(pacific_arr, True)
        bfs(atlantic_arr,False)

        output_set = pacific_seen & atlantic_seen
        
        return [list(item) for item in output_set]
            



        
        #call bfs over each of the tuples in pacific (with is_pacific = True)
        #call bfs over each of the tuples in atlantic (with is_pacific = False)
        