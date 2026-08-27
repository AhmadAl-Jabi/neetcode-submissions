class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # this time we can call the same index many times cuz we can have dupe numbers
        output_arr = []

        def dfs(start_index, curr_arr, curr_total):
            # if curr_total we got is too much return
            if curr_total > target:
                return

            # if curr_total we got is equal target --> append to output_arr a copy and return
            if curr_total == target:
                output_arr.append(curr_arr.copy())
                return
            
            # otherwise we just keep exploring options ranging from start_index onward (this is to avoid dupe answers like [1,2] [2,1])
            for i in range(start_index, len(nums)):

                temp_total = curr_total + nums[i]
                curr_arr.append(nums[i])

                dfs(i,curr_arr,temp_total)

                curr_arr.pop()
            
        
        dfs(0, [], 0)
        return output_arr

 



        