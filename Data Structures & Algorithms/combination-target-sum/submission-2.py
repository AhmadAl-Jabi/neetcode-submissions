class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # numbers are unique (no dupes)
        # want all combinations (list of lists) where the numbers sum to target
        # can reuse a specific number many times
        # two combinations are the same if equal frequencies of every character (e.g. [2,3,2] same as [2,2,3]) order d/n matter
        # might have to deal with sets (uniqueness) --> don't think we'll need to because order probably won't be an issue

        # all combinations --> backtracking problem (attempt a combination and go back when we fail)
        # [2,5,6,9] 
        # [9]
        # target = 9

        # explore a path as deep as possible and go back when sum is too big
        # recursively
        # start_idx is the first idx we're allowed to use in the current iteration (avoids dupe combinations)
        curr_comb = []
        output_arr = []

        def dfs(start_idx, curr_sum):
            if curr_sum >= target:
                if curr_sum == target:
                    output_arr.append(curr_comb.copy())
                return

            for i in range(start_idx, len(nums)):
                # add new number to curr_comb
                curr_comb.append(nums[i])
                dfs(i, curr_sum + nums[i])

                # pop new number from curr_comb
                curr_comb.pop()

        dfs(0, 0)
        return output_arr


