class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # since we can't have duplicates, for each index we should only look at i + 1 onwards (never back)

        # we should also append copies of the curr_arr each time rather than the original (since that will get mutated)

        output_arr = [[]]

        def dfs(start_index, curr_arr):
            
            for i in range(start_index, len(nums)):
                
                curr_arr.append(nums[i])
                output_arr.append(curr_arr.copy())

                # index + 1 since we do NOT want to revisit current index again
                dfs(i+1, curr_arr)

                # after going as deep as possible in this path we pop from curr_arr 
                curr_arr.pop()
            

        dfs(0,[])
        return output_arr
            


            


