class Solution:
    def rob(self, nums: List[int]) -> int:
        # I was thinking of doing smt similar to the climbing stairs
        # but doing nums[i] + max(dfs(i+2), dfs(i+3)) 
        # since we cant rob i+1 AND delaying past i+3 is stupid
        # since we could just do i+2 and i+4
        n = len(nums)
        cache = [-1] * n

        def dfs(i):

            if i >= n: # We went out of bounds
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = nums[i] + max(dfs(i+2), dfs(i+3)) # We don't do i+4 since we could do two i+2's
            return cache[i]
        
        return max(dfs(0), dfs(1))
        