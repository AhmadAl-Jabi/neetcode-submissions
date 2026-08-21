class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Lowkey not too bad. I'm thinking of going through the arrays and basically just storing the max val inside
        # If the target is too big for the max of this guy, then move to the next
        # Keep doing this until the max of the subarray is good --> Problem tho is the time complexity

        # Instead we work with left and right pointers and take the mid subarray. Take its first and last indices
        # Check if the target is in between the two, if so, good, if it's bigger then we left = mid + 1 or smaller then right = mid -1
        # Once we find the good subarray we just need normal ahh binary search inside the subarray which will also be log(n)

        out_left = 0
        out_right = len(matrix) - 1

        while out_left <= out_right:

            out_mid = (out_left + out_right)//2
            mid_arr = matrix[out_mid]

            if mid_arr[0] <= target <= mid_arr[-1]:
                in_left = 0
                in_right = len(mid_arr) - 1

                while in_left <= in_right:
                    in_mid = (in_left + in_right)//2
                    mid_item = mid_arr[in_mid]

                    if target == mid_item:
                        return True
                    
                    elif target > mid_item:
                        in_left = in_mid + 1
                    
                    else:
                        in_right = in_mid - 1

                return False # No need to check any other subarrays and waste time if we didn't find it here

            elif target > mid_arr[-1]: # If the target bigger than the biggest guy there
                out_left = out_mid + 1
            
            else:
                out_right = out_mid - 1

        return False