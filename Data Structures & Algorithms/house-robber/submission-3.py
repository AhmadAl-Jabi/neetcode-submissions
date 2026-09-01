class Solution:
    def rob(self, nums: List[int]) -> int:
        # keep in mind you do not necessarily have to rob every i + 2 house. You can choose to skip whenever
        # can go as deep as possible and start from the end to see max value if this house robbed
        # for each choice we make we check i + 2 and i + 3. The reason we do this is because i + 4 is just i + 2 twice, and i + 1 is not allowed, so those are realistically our only 2 good options
        

        # can lowkey do the same approach as last question and just act like we can only go left to right (doesn't change soln)

        next_1, next_2 = 0, 0

        # [10, 1, 2, 900, 10] None, None, None
        #                 cur       next_1 next_2   
        #            cur      next_1 next_2
        #         cur    next_1 next_2

        for i in range(len(nums) - 1, -1, -1):
            curr_sum = nums[i] + max(next_1, next_2)
            nums[i] = curr_sum

            next_2 = next_1
            next_1 = nums[i + 1] if (i + 1) < len(nums) else 0

        return max(nums[0], nums[1]) if len(nums) > 1 else nums[0]



        