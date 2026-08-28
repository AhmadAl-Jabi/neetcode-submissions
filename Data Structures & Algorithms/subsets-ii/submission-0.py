class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output_arr = []

        def dfs(start_index, curr_arr):
            # Every current path represents a valid subset
            output_arr.append(curr_arr.copy())

            for i in range(start_index, len(nums)):

                # Skip duplicate choices at the same level
                if i > start_index and nums[i] == nums[i - 1]:
                    continue

                curr_arr.append(nums[i])

                # i + 1 because each index can only be used once
                dfs(i + 1, curr_arr)

                curr_arr.pop()

        dfs(0, [])
        return output_arr
        