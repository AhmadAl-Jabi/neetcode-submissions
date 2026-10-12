class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # Another approach maybe using bits --> track which one is missing
        # number xor with itself is 0 --> we can use that

        # what number can we start with to xor with the values in nums
        # can use the fact that if we had a full [0,n] range then every single number would match its index
        #n=3 -> [0,1,2,3]
        # nums is len(n) --> we do NOT have an index n 
        # our real nums will NOT have this for every number since one has to be missing -> n

        # Algorithm
        # we can walk through nums and maintain a nums_result of xoring everything
        # and at the same time maintain a n_xor result of xoring every number from 0 to n inclusive

        # xor the two at the end and the result of that should be the missing number since we'd have pairs except for the missing number (shows up once in n_xor)

        n_xor = len(nums)
        nums_result = 0

        for i in range(len(nums)):
            n_xor ^= i
            nums_result ^= nums[i]
        
        return n_xor ^ nums_result