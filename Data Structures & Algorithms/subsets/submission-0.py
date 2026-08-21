class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # We have 2^n possibilities cuz at each number n we have 2 choices (include or exclude)
        # So we have 2 choices n times (2*2*2*2... = 2^n)

        final_arr = []
        curr_sub = []


        def dfs(i):

            if i >= len(nums):
                final_arr.append(curr_sub.copy())
                return

            curr_sub.append(nums[i])

            dfs(i+1) # So go deeper with the choice of keeping the number
            curr_sub.pop()
            dfs(i+1) # Go deeper with the choice of excluding the number

            # It may seem confusing trying to think of the 2^n possibilities, but basically
            # At each time there is a branch split and we should just think of i as a number that advances
            # For the branch where we always exclude it will be completely empty when we hit the base case
            # But that branch will also have a split right before the base case where it will at least append the last num
            # Then it will hit base case and return
        
        dfs(0)
        return final_arr
            
