class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # since we can't have duplicates, for each index we should only look at i + 1 onwards (never back)

        # we should also append copies of the curr_arr each time rather than the original (since that will get mutated)

        output_arr = []
        seen_indices = set()

        def dfs(start_index, curr_arr):

            if start_index in seen_indices:
                return
            
            output_arr.append(curr_arr.copy())

            for i in range(start_index + 1, len(nums)):
                
                seen_indices.add(i-1)
                curr_arr.append(nums[i-1])

                # index + 1 since we do NOT want to revisit current index again
                dfs(i, curr_arr)

                # after going as deep as possible in this path we pop from curr_arr and 
                seen_indices.discard(i-1)
                curr_arr.pop()
            

        dfs(-1,[])
        return output_arr
            


            


