class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = float("-inf")
        cur_sum = float("-inf")

        for i in range(len(nums)):
            # if the cur_sum is negative no matter what we're better getting rid of it at the current number
            if cur_sum < 0:
                cur_sum = nums[i]

            else:
                cur_sum += nums[i]
            
            max_total = max(max_total, cur_sum)

        return max_total
