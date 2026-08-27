class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # this time we can't call the same index many times cuz we can not have dupe numbers
        output_arr = []
        candidates.sort()

        def dfs(start_index, curr_arr, curr_total):
            # if curr_total we got is too much return
            if curr_total > target:
                return

            # if curr_total we got is equal target --> append to output_arr a copy and return
            if curr_total == target:
                output_arr.append(curr_arr.copy())
                return
            
            # otherwise we just keep exploring options ranging from start_index onward (this is to avoid dupe answers like [1,2] [2,1])
            for i in range(start_index, len(candidates)):
                # i > start_index basically says if i is bigger than our cutrent depth AND its a dupe then skip. otherwise if the current depth is a dupe its okay (e.g [2,2,2,3] when start_index is 0 then 2 is allowed and 1 > 0 is not allowed as a dupe. but when we traverse to depth 1 and start index is 1, its okay if 2 is a dupe of prev cuz we allow the first dupe of a depth. but the next 2 (i=2) is NOT ALLOWED at this depth. but when we tracerse its allowrd)
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue

                temp_total = curr_total + candidates[i]

                curr_arr.append(candidates[i])

                dfs(i+1,curr_arr,temp_total)

                curr_arr.pop()
            
        
        dfs(0, [], 0)
        return output_arr

 



        