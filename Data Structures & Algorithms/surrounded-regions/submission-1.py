from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        seen = set() # -> This will let us track the coords of 0's that ARE connected to edges
        queue = deque()

        # go across all 4 edges and add to queue the circles that we see and add to seen
        for j in range(len(board[0])):
            if board[0][j] == "O":
                seen.add((0,j))
                queue.append((0,j))
            if board[len(board) - 1][j] == "O":
                seen.add(((len(board) - 1), j))
                queue.append(((len(board) - 1), j))

        for i in range(len(board)):
            if board[i][0] == "O":
                seen.add((i,0))
                queue.append((i,0))

            if board[i][len(board[0]) - 1] == "O":
                seen.add((i,len(board[0]) - 1))
                queue.append((i,len(board[0]) - 1))

        def bfs(queue):
            while queue:
                row, col = queue.popleft()
                for direction in dirs:
                    dr, dc = direction[0] + row, direction[1] + col

                    if dr < 0 or dc < 0 or dr >= len(board) or dc >= len(board[0]) or board[dr][dc] == "X" or (dr,dc) in seen:
                        continue

                    # otherwise add it to seen
                    seen.add((dr,dc))
                    # append it to queue
                    queue.append((dr,dc))

        bfs(queue)

        # one last traversal over everything in board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in seen and board[i][j] == "O":
                    board[i][j] = "X"



        