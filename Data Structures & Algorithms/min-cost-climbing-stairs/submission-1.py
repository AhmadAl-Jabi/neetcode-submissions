class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-100] * n

        testing_array = []
        
        def dfs(i):
            nonlocal cache

            if i >= n:
                return 0 # this means we are out of bounds so we return 0 (finished staircase)
            if cache[i] != -100: # this means we've already seen this i and calculated its min cost
                return cache[i]
            
            cache[i] = cost[i] + min(dfs(i+1), dfs(i+2)) #gotta pay the price even if at the end, THEN we move
            return cache[i]

        testing_array.append(dfs(0))
        testing_array.append(dfs(1))
        return min(testing_array)

        return min(dfs(0), dfs(1))


        