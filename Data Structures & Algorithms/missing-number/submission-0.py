class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) # --> we include n in the range [0,n]

        nums_xor = 0 # the numbers in nums xor with each other
        n_xor = 0 # all numbers in range n (including the missing) xor with each other

        for i in range(n + 1):
            nums_xor ^= nums[i] if i < n else 0
            n_xor ^= i


        missing_num = n_xor ^ nums_xor
        return missing_num