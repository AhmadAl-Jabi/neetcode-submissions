from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        queue = deque() # stores row, col, level and nodes seen on path
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        # Can't have one global seen. Need one for each path basically

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    queue.append((i,j,0,set((i,j))))

        def bfs():
            
            while queue:
                curr_node = queue.popleft()
                o_row, o_col, curr_level, seen = curr_node[0], curr_node[1], curr_node[2], curr_node[3]
                seen.add((o_row,o_col)) # no need to remove later since each source only goes down proper paths and has their own set

                if curr_level == (len(word) - 1):
                    return True
                
                for direction in dirs:
                    dr, dc = o_row + direction[0], o_col + direction[1]

                    if dr < 0 or dc < 0 or dr >= len(board) or dc >= len(board[0]) or board[dr][dc] != word[curr_level + 1] or (dr,dc) in seen:
                        continue

                    new_set = set(seen)
                    queue.append((dr,dc,curr_level + 1, new_set))
            return False
            
        return bfs()


