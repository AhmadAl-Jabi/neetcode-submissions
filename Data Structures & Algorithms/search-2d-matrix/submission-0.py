class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # We do binary search on the arrays themselves (outer_left & outer_right)
        # Basically look at the middle array of the two and investigate

        # If target is in between inner_left and inner_right of that array
        # do normal binary search and either return True or False (can't be elsewhere)

        # else if target is bigger than right we do outer_left = out_mid + 1
        # else if target is smaller than left we do outer_right = out_mid - 1

        # Note: do >= for both inner and outer conditions

        outer_left, outer_right = 0, len(matrix) - 1

        while outer_left <= outer_right:

            outer_mid = (outer_left + outer_right) // 2
            inner_left, inner_right = 0, len(matrix[0]) - 1

            # If target in range, investigate
            if target <= matrix[outer_mid][inner_right] and target >= matrix[outer_mid][inner_left]:

                curr_matrix = matrix[outer_mid] # For simplicity; won't change

                # Perform normal binary search on the inner matrix (True or False)
                while inner_left <= inner_right:

                    inner_mid = (inner_left + inner_right) // 2

                    if curr_matrix[inner_mid] == target:
                        return True
                    
                    elif curr_matrix[inner_mid] > target:
                        inner_right = inner_mid - 1
                    
                    else:
                        inner_left = inner_mid + 1
                
                break #break out of larger while loop and return False if not found

            # Otherwise save time and skip

            elif target < matrix[outer_mid][inner_left]:
                outer_right = outer_mid - 1
            
            elif target > matrix[outer_mid][inner_right]:
                outer_left = outer_mid + 1


        return False
        