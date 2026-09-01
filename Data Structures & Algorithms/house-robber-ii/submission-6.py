class Solution:
    def rob(self, nums: List[int]) -> int:

        # can have case where we "start" at 0
        # can have case where we "start" at 1
        # [1,2,3,4,5]

        if len(nums) <= 3:
            return max(nums)

        def iterative_soln(copy, start_index):
            next_1, next_2 = 0,0

            for i in range(start_index, -1, -1):
                copy[i] += max(next_1, next_2)
                next_2 = next_1
                next_1 = copy[i+1] if (i+1) <= start_index else 0 

            if start_index == len(copy) - 1:
                return max(copy[1], copy[2])
            
            return max(copy[0],copy[1])
        
        # make a copy of nums before passing it

        # case of NOT robbing house 0
        result_1 = iterative_soln(nums.copy(), len(nums) - 1)

        # case of robbing house 0
        result_2 = iterative_soln(nums.copy(), len(nums) - 2)

        return max(result_1, result_2)













