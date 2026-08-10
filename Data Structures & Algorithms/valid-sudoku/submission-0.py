class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # I guess we can check every row one by one using sets and seeing if the length is the same
        # Can do the same for columns but one at a time basically
        # can use modulo for the 3x3 squares

        # Be careful with the "." since they only show up once in set but multiple in rows/columns so let's just track the numbers alone instead


        isValid = True
        # Row
        for row in board:
            seen = set()

            for x in row:
                if x in seen:
                    return False

                if x != ".":
                    seen.add(x)
            
        # Column
        for j in range(len(board[0])): # j is the column not the row

            seen = set()

            for i in range(len(board)):
                if board[i][j] in seen:
                    return False
                
                if board[i][j] != ".":
                    seen.add(board[i][j])


        # Squares --> Can use integer division (//3) so that each number belongs
        # To the right square

        for box_r in range(3):
            for box_c in range(3):

                seen = set()

                for i in range(box_r * 3,box_r * 3 + 3):
                    for j in range(box_c * 3,box_c * 3 + 3):

                        if board[i][j] in seen:
                            return False
                
                        if board[i][j] != ".":
                            seen.add(board[i][j])

        return isValid
        