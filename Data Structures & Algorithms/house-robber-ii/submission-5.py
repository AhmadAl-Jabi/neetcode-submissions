class Solution:
    def rob(self, nums: List[int]) -> int:

        # Literally the only thing that changed now is that if we choose the first house, we cannot choose the last house too
        # That's it
        # I can do a somewhat tacky solution and pass "is 0" to be like ok new base case only when we call dfs(0) 
        
        n = len(nums)

        if n == 1:
            return nums[0]

        cache = [[-1] * 2 for num in nums] # 2D array cuz the cache for dfs(0) MUST be diff than the one for dfs(1) since they can produce diff results

        def dfs(i, incl_first):

            if i >= n or (incl_first and (i == n - 1)): # We went out of bounds
                return 0
            
            if cache[i][incl_first] != -1:
                return cache[i][incl_first]
            
            cache[i][incl_first] = max(dfs(i+1, incl_first), nums[i] + dfs(i+2, incl_first)) # We don't do i+4 since we could do two i+2's
            return cache[i][incl_first]
        
        return max(dfs(0, True), dfs(1, False))