class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = ((1,0),(0,1),(-1,0),(0,-1))

        # we want to store the (row,col) visited for pacific and for atlantic separately
        pacific_seen, atlantic_seen = set(), set()
        # first row elements
        for col in range(cols):
            pacific_seen.add((0,col))
        for row in range(rows):
            pacific_seen.add((row,0))

        for col in range(cols):
            atlantic_seen.add((rows - 1,col))
        for row in range(rows):
            atlantic_seen.add((row,cols -1))

        for curr_set in (pacific_seen,atlantic_seen):
            queue = deque(curr_set)
            while queue:
                curr_element = queue.popleft()
                row, col = curr_element[0], curr_element[1]
                    
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    if new_row < 0 or new_col < 0 or new_row >= rows or new_col >= cols or (new_row, new_col) in curr_set or heights[new_row][new_col] < heights[row][col]:
                        continue

                    # add the neighbour to our queue 
                    curr_set.add((new_row,new_col))
                    queue.append((new_row,new_col))
            # now we want to return the cells that were in both groups
        output_arr = []
        for row in range(rows):
            for col in range(cols):
                if (row,col) in pacific_seen and (row,col) in atlantic_seen:
                    output_arr.append([row,col])
        return output_arr
