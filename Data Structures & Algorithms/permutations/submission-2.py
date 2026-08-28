class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        output_arr = []

        def dfs(curr_arr, seen):

            # full permutation built

            if len(curr_arr) == len(nums):

                output_arr.append(curr_arr.copy())

                return

            # every level can consider every index

            for i in range(len(nums)):

                if i in seen:

                    continue

                curr_arr.append(nums[i])

                seen.add(i)

                dfs(curr_arr, seen)

                # backtrack

                seen.remove(i)

                curr_arr.pop()

        dfs([], set())

        return output_arr
        