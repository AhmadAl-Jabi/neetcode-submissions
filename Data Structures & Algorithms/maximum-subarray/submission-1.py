class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = float("-inf")
        cur_sum = 0

        for i in range(len(nums)):
            # if the cur_sum is negative no matter what we're better getting rid of it at the current number
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_total = max(max_total, cur_sum)

        return max_total
